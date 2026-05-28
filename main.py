"""
main.py  —  SecureITLab Proposal Generator Backend
Run with:  uvicorn main:app --reload --port 8000
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List, Optional
import io, os

from docx import Document
from docx.shared import Pt, RGBColor, Cm, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from lxml import etree

from proposal_data import PROPOSALS

# ── Colour helpers ──────────────────────────────────────────────────────────
NAVY   = RGBColor(0x1A, 0x3C, 0x6E)
BLUE   = RGBColor(0x2E, 0x75, 0xB6)
LBLUE  = RGBColor(0xD5, 0xE8, 0xF0)
GREY   = RGBColor(0x59, 0x59, 0x59)
WHITE  = RGBColor(0xFF, 0xFF, 0xFF)

NAVY_HEX  = "1A3C6E"
BLUE_HEX  = "2E75B6"
LBLUE_HEX = "D5E8F0"
GREY_HEX  = "595959"
WHITE_HEX = "FFFFFF"
CC_HEX    = "CCCCCC"

# ── Pydantic models ─────────────────────────────────────────────────────────
class CostRow(BaseModel):
    item: str = ""
    desc: str = ""
    unit_price: float = 0
    qty: int = 1
    total: float = 0

class TimelineRow(BaseModel):
    phase: str = ""
    activities: str = ""
    duration: str = ""
    deliverables: str = ""

class ProposalRequest(BaseModel):
    # Service
    service_key: str                     # key from PROPOSALS dict
    service_name: str
    service_desc: str
    service_deliverables: List[str] = []

    # Organisation
    org_name: str = ""
    org_industry: str = ""
    org_address: str = ""
    org_contact: str = ""
    org_email: str = ""
    org_phone: str = ""
    org_bg: str = ""
    org_obj: str = ""

    # Proposal meta
    prop_date: str = ""
    prop_ref: str = ""
    start_date: str = ""
    end_date: str = ""
    currency: str = "USD"
    tax_rate: float = 0

    # Scope lists
    inscope: List[str] = []
    outscope: List[str] = []
    assumptions: List[str] = []
    responsibilities: List[str] = []
    payments: List[str] = []

    # Tables (user-customised; if empty, use proposal_data defaults)
    timeline_rows: List[TimelineRow] = []
    cost_rows: List[CostRow] = []

# ── FastAPI app ─────────────────────────────────────────────────────────────
app = FastAPI(title="SecureITLab Proposal Generator", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],          # tighten for production
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve the HTML front-end at /
if os.path.exists("SecureITLab_Proposal_Generator.html"):
    from fastapi.responses import FileResponse
    @app.get("/")
    def serve_frontend():
        return FileResponse("SecureITLab_Proposal_Generator.html")

# ── Endpoint: list available services ───────────────────────────────────────
@app.get("/services")
def list_services():
    return {k: {"phases": len(v["timeline"])} for k, v in PROPOSALS.items()}

# ── Endpoint: get methodology + timeline for a service ───────────────────────
@app.get("/services/{key}")
def get_service(key: str):
    if key not in PROPOSALS:
        raise HTTPException(404, f"Service key '{key}' not found")
    data = PROPOSALS[key]
    return {
        "methodology": data["methodology"],
        "timeline": [
            {"phase": t[0], "activities": t[1], "duration": t[2], "deliverables": t[3]}
            for t in data["timeline"]
        ]
    }

# ── Endpoint: generate proposal docx ────────────────────────────────────────
@app.post("/generate")
def generate_proposal(req: ProposalRequest):
    if req.service_key not in PROPOSALS:
        raise HTTPException(404, f"Service key '{req.service_key}' not found")

    proposal_data = PROPOSALS[req.service_key]

    # Use timeline from proposal_data if user didn't customise
    if not req.timeline_rows:
        timeline = [
            TimelineRow(phase=t[0], activities=t[1], duration=t[2], deliverables=t[3])
            for t in proposal_data["timeline"]
        ]
    else:
        timeline = req.timeline_rows

    buf = build_docx(req, proposal_data, timeline)

    safe_name = (req.org_name or "Proposal").replace(" ", "_")
    safe_svc  = req.service_name.replace(" ", "_").replace("/", "-")
    filename  = f"Proposal_{safe_name}_{safe_svc}.docx"

    return StreamingResponse(
        buf,
        media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        headers={"Content-Disposition": f'attachment; filename="{filename}"'},
    )

# ── Document builder ─────────────────────────────────────────────────────────
def build_docx(req: ProposalRequest, proposal_data: dict, timeline: list) -> io.BytesIO:
    doc = Document()

    # ── Page setup (A4, 2.5 cm margins) ─────────────────────────────────────
    for section in doc.sections:
        section.page_width  = Cm(21)
        section.page_height = Cm(29.7)
        section.top_margin = section.bottom_margin = Cm(2.5)
        section.left_margin = section.right_margin = Cm(2.5)

    # ── Document-wide default font ───────────────────────────────────────────
    style = doc.styles["Normal"]
    style.font.name = "Arial"
    style.font.size = Pt(10)

    # ── Header & footer ──────────────────────────────────────────────────────
    hdr = doc.sections[0].header
    hdr_para = hdr.paragraphs[0]
    hdr_para.clear()
    _add_run(hdr_para, f"SecureITLab — Confidential     |     {req.service_name}",
             size=8, colour=GREY)
    _bottom_border(hdr_para, BLUE_HEX, 6)

    ftr = doc.sections[0].footer
    ftr_para = ftr.paragraphs[0]
    ftr_para.clear()
    _add_run(ftr_para, f"www.secureitlab.com     |     {req.org_name}     |     {req.prop_date}",
             size=8, colour=GREY)
    _top_border(ftr_para, CC_HEX, 4)

    # ══════════════════════════════════════════════════════════════════
    # COVER PAGE
    # ══════════════════════════════════════════════════════════════════
    _spacer(doc, 6)
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    _add_run(p, "SecureITLab", size=28, bold=True, colour=NAVY)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    _add_run(p, "Cybersecurity  |  Data Privacy  |  Data Governance", size=11, colour=BLUE)
    _bottom_border(p, BLUE_HEX, 6)

    _spacer(doc, 3)
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    _add_run(p, "SERVICE PROPOSAL", size=14, bold=True, colour=GREY)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    _add_run(p, req.service_name, size=18, bold=True, colour=NAVY)
    _bottom_border(p, BLUE_HEX, 6)

    _spacer(doc, 2)
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    _add_run(p, "Prepared for:", size=11, colour=GREY)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    _add_run(p, req.org_name, size=16, bold=True, colour=NAVY)

    _spacer(doc, 1)
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    _add_run(p, f"Proposal Date: {req.prop_date}", size=10, colour=GREY)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    _add_run(p, f"Reference: {req.prop_ref}", size=10, colour=GREY)

    doc.add_page_break()

    # ══════════════════════════════════════════════════════════════════
    # S1  Organisation Overview
    # ══════════════════════════════════════════════════════════════════
    _heading(doc, "1.  Organisation Overview")
    _rule(doc)

    fields = [
        ("Organisation Name", req.org_name),
        ("Industry / Sector",  req.org_industry),
        ("Registered Address", req.org_address),
        ("Primary Contact",    req.org_contact),
        ("Email",              req.org_email),
        ("Phone",              req.org_phone),
        ("Organisation Background", req.org_bg),
        ("Engagement Objective",    req.org_obj),
    ]
    for label, val in fields:
        p = doc.add_paragraph()
        _add_run(p, f"{label}:  ", bold=True, colour=NAVY)
        _add_run(p, val or "—", colour=GREY)

    doc.add_page_break()

    # ══════════════════════════════════════════════════════════════════
    # S2  About SecureITLab  (boilerplate)
    # ══════════════════════════════════════════════════════════════════
    _heading(doc, "2.  About SecureITLab")
    _rule(doc)

    _body(doc, ("SecureITLab is a remote-first cybersecurity, data privacy, and data governance "
                "consulting firm with over 20 years of industry experience. Headquartered in the "
                "Kingdom of Bahrain, with offices in the Philippines and India, SecureITLab serves "
                "clients across the Middle East, Asia-Pacific, and beyond."))
    _body(doc, ("Our team of certified professionals (CISSP, CISM, CISA, CEH, ISO 27001 LA/LI, CDPSE) "
                "delivers tailored, risk-driven solutions that empower organisations to navigate the "
                "complex landscape of cybersecurity and compliance with confidence."))
    _body(doc, "SecureITLab is certified to ISO 27001:2022, ISO 27701:2019, and ISO 22301:2019.")

    _subheading(doc, "Core Capabilities")
    caps = [
        "Consulting — Cybersecurity and Data Privacy",
        "Assurance — Penetration Testing, Vulnerability Assessment and Red Teaming",
        "Audit and Compliance — IT Audit, Cloud Audit and ISO Compliance",
        "Services Augmentation — vCISO, vCDO and Expert Resourcing",
        "Managed Services — SOC, NOC, Vulnerability Management and Take-Down",
    ]
    for c in caps:
        _bullet(doc, c)

    doc.add_page_break()

    # ══════════════════════════════════════════════════════════════════
    # S3  Service Description
    # ══════════════════════════════════════════════════════════════════
    _heading(doc, "3.  Service Description")
    _rule(doc)

    p = doc.add_paragraph()
    _add_run(p, req.service_name, size=12, bold=True, colour=BLUE)
    _body(doc, req.service_desc)

    _subheading(doc, "Key Deliverables")
    for d in req.service_deliverables:
        _bullet(doc, d)

    _subheading(doc, "Methodology")
    _body(doc, ("SecureITLab employs industry-recognised methodologies, standards, and frameworks "
                "throughout this engagement. All activities are conducted in alignment with the agreed "
                "scope and subject to the client's change-control and information security policies."))
    for phase_text in proposal_data["methodology"]:
        _body(doc, phase_text)

    doc.add_page_break()

    # ══════════════════════════════════════════════════════════════════
    # S4  Scope of Work
    # ══════════════════════════════════════════════════════════════════
    _heading(doc, "4.  Scope of Work")
    _rule(doc)
    _body(doc, "Define the precise boundaries of the engagement. Items not listed are considered out of scope.")

    _subheading(doc, "In Scope")
    _bullet_list(doc, req.inscope, fallback="To be defined.")

    _subheading(doc, "Out of Scope")
    _bullet_list(doc, req.outscope, fallback="To be defined.")

    _subheading(doc, "Assumptions and Dependencies")
    _bullet_list(doc, req.assumptions, fallback="To be confirmed.")

    _subheading(doc, "Client Responsibilities")
    _bullet_list(doc, req.responsibilities, fallback="To be confirmed.")

    doc.add_page_break()

    # ══════════════════════════════════════════════════════════════════
    # S5  Project Timeline
    # ══════════════════════════════════════════════════════════════════
    _heading(doc, "5.  Project Timeline")
    _rule(doc)
    _body(doc, "The indicative timeline below is subject to confirmation upon contract award.")

    p = doc.add_paragraph()
    _add_run(p, "Proposed Start: ", bold=True, colour=NAVY)
    _add_run(p, req.start_date or "TBD", colour=GREY)
    _add_run(p, "     Proposed End: ", bold=True, colour=NAVY)
    _add_run(p, req.end_date or "TBD", colour=GREY)

    # Timeline table
    col_w = [Cm(3.2), Cm(6.2), Cm(2.8), Cm(5.5)]
    tbl = doc.add_table(rows=1, cols=4)
    tbl.alignment = WD_TABLE_ALIGNMENT.LEFT
    _set_col_widths(tbl, col_w)

    hdr_cells = tbl.rows[0].cells
    for i, h in enumerate(["Phase", "Activities", "Duration", "Deliverables"]):
        _header_cell(hdr_cells[i], h, col_w[i])

    for idx, row in enumerate(timeline):
        cells = tbl.add_row().cells
        fill = LBLUE_HEX if idx % 2 == 1 else WHITE_HEX
        _data_cell(cells[0], row.phase,        col_w[0], fill)
        _data_cell(cells[1], row.activities,   col_w[1], fill)
        _data_cell(cells[2], row.duration,     col_w[2], fill)
        _data_cell(cells[3], row.deliverables, col_w[3], fill)

    doc.add_page_break()

    # ══════════════════════════════════════════════════════════════════
    # S6  Investment Summary
    # ══════════════════════════════════════════════════════════════════
    _heading(doc, "6.  Investment Summary")
    _rule(doc)
    _body(doc, "All fees are exclusive of applicable taxes. Payment terms are as per the Master Service Agreement or as agreed in writing.")

    p = doc.add_paragraph()
    _add_run(p, f"Currency: {req.currency}", bold=True, colour=NAVY)

    cost_rows = req.cost_rows
    subtotal  = sum(r.total for r in cost_rows)
    tax_amt   = round(subtotal * req.tax_rate / 100, 2)
    grand     = round(subtotal + tax_amt, 2)

    ccol = [Cm(4.2), Cm(5.4), Cm(2.8), Cm(1.6), Cm(3.7)]
    ctbl = doc.add_table(rows=1, cols=5)
    ctbl.alignment = WD_TABLE_ALIGNMENT.LEFT
    _set_col_widths(ctbl, ccol)

    ch = ctbl.rows[0].cells
    for i, h in enumerate(["Line Item", "Description", "Unit Price", "Qty", f"Total ({req.currency})"]):
        _header_cell(ch[i], h, ccol[i])

    for idx, r in enumerate(cost_rows):
        cells = ctbl.add_row().cells
        fill  = LBLUE_HEX if idx % 2 == 1 else WHITE_HEX
        _data_cell(cells[0], r.item,             ccol[0], fill)
        _data_cell(cells[1], r.desc,             ccol[1], fill)
        _data_cell(cells[2], _fmt(r.unit_price), ccol[2], fill)
        _data_cell(cells[3], str(r.qty),         ccol[3], fill)
        _data_cell(cells[4], _fmt(r.total),      ccol[4], fill)

    # Subtotal / tax / grand total rows
    _summary_row(ctbl, ccol, f"Subtotal",           _fmt(subtotal), LBLUE_HEX, NAVY_HEX)
    _summary_row(ctbl, ccol, f"Tax ({req.tax_rate}%)", _fmt(tax_amt), LBLUE_HEX, NAVY_HEX)
    _summary_row(ctbl, ccol, "TOTAL INVESTMENT",
                 f"{req.currency} {_fmt(grand)}", NAVY_HEX, WHITE_HEX, bold_label=True)

    _subheading(doc, "Payment Schedule")
    _bullet_list(doc, req.payments, fallback="As agreed.")
    _body(doc, "Validity: This proposal is valid for 30 days from the date of issue.")

    doc.add_page_break()

    # ══════════════════════════════════════════════════════════════════
    # S7  Terms and Conditions  (boilerplate)
    # ══════════════════════════════════════════════════════════════════
    _heading(doc, "7.  Terms and Conditions")
    _rule(doc)
    _body(doc, ("This proposal is subject to SecureITLab's standard Master Service Agreement (MSA). "
                "Key terms are summarised below; the MSA governs in the event of any conflict."))

    tc_items = [
        ("Confidentiality",
         "Both parties agree to maintain strict confidentiality of all information exchanged. "
         "SecureITLab will not disclose client data to third parties without prior written consent."),
        ("Intellectual Property",
         "All deliverables become the property of the client upon receipt of full payment. "
         "SecureITLab retains rights to its pre-existing methodologies, tools, and frameworks."),
        ("Limitation of Liability",
         "SecureITLab's aggregate liability shall not exceed the total fees paid under this engagement. "
         "SecureITLab is not liable for indirect, consequential, or incidental damages."),
        ("Governing Law",
         "This proposal and any resulting engagement shall be governed by the laws of the Kingdom of "
         "Bahrain, unless otherwise agreed in writing."),
        ("Amendments",
         "Any change in scope, timeline, or cost requires a written Change Request signed by both "
         "parties prior to implementation."),
    ]
    for title, body in tc_items:
        p = doc.add_paragraph()
        _add_run(p, f"{title}:  ", bold=True, colour=NAVY)
        _add_run(p, body, colour=GREY)

    doc.add_page_break()

    # ══════════════════════════════════════════════════════════════════
    # S8  Acceptance and Signatures
    # ══════════════════════════════════════════════════════════════════
    _heading(doc, "8.  Acceptance and Signatures")
    _rule(doc)
    _body(doc, ("By signing below, both parties confirm their agreement to the terms set out in this "
                "proposal and authorise SecureITLab to commence the engagement as described."))

    _spacer(doc, 2)

    sig_col = [Cm(7.5), Cm(2.0), Cm(7.5)]
    stbl = doc.add_table(rows=4, cols=3)
    _set_col_widths(stbl, sig_col)

    header_row = stbl.rows[0]
    _sig_header_cell(header_row.cells[0], f"Authorised Signatory — {req.org_name}", sig_col[0])
    _sig_header_cell(header_row.cells[2], "Authorised Signatory — SecureITLab",     sig_col[2])

    for row in stbl.rows[1:]:
        for cell in row.cells:
            cell.text = ""

    _spacer(doc, 2)
    _rule(doc)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    _add_run(p, "SecureITLab  |  info@secureitlab.com  |  www.secureitlab.com", size=9, colour=GREY)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    _add_run(p, "Bahrain  |  Philippines  |  India", size=9, colour=GREY)

    buf = io.BytesIO()
    doc.save(buf)
    buf.seek(0)
    return buf


# ── Low-level helpers ────────────────────────────────────────────────────────

def _add_run(para, text, size=10, bold=False, italic=False, colour=None):
    run = para.add_run(text)
    run.font.name = "Arial"
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.italic = italic
    if colour:
        run.font.color.rgb = colour
    return run

def _heading(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(14)
    p.paragraph_format.space_after  = Pt(6)
    _add_run(p, text, size=14, bold=True, colour=NAVY)

def _subheading(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after  = Pt(4)
    _add_run(p, text, size=11, bold=True, colour=NAVY)

def _body(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after  = Pt(4)
    _add_run(p, text, colour=GREY)

def _bullet(doc, text):
    p = doc.add_paragraph(style="List Bullet")
    _add_run(p, text, colour=GREY)

def _bullet_list(doc, items, fallback=""):
    clean = [i for i in items if i.strip()]
    if clean:
        for item in clean:
            _bullet(doc, item)
    elif fallback:
        _body(doc, fallback)

def _spacer(doc, lines=1):
    for _ in range(lines):
        doc.add_paragraph()

def _rule(doc):
    p = doc.add_paragraph()
    _bottom_border(p, BLUE_HEX, 6)

def _fmt(val):
    return f"{val:,.2f}"

def _bottom_border(para, colour_hex, size):
    pPr = para._p.get_or_add_pPr()
    pBdr = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), str(size))
    bottom.set(qn("w:space"), "1")
    bottom.set(qn("w:color"), colour_hex)
    pBdr.append(bottom)
    pPr.append(pBdr)

def _top_border(para, colour_hex, size):
    pPr = para._p.get_or_add_pPr()
    pBdr = OxmlElement("w:pBdr")
    top = OxmlElement("w:top")
    top.set(qn("w:val"), "single")
    top.set(qn("w:sz"), str(size))
    top.set(qn("w:space"), "1")
    top.set(qn("w:color"), colour_hex)
    pBdr.append(top)
    pPr.append(pBdr)

def _set_col_widths(table, widths):
    tbl_el = table._tbl
    tblPr  = tbl_el.find(qn("w:tblPr")) or OxmlElement("w:tblPr")
    tblW   = OxmlElement("w:tblW")
    total  = sum(int(w.cm * 914400 / 360) for w in widths)   # EMU → twips approx
    tblW.set(qn("w:w"),    str(total))
    tblW.set(qn("w:type"), "dxa")
    tblPr.append(tblW)

def _twips(cm_val):
    return int(cm_val.cm * 567)   # 1 cm ≈ 567 twips

def _shade_cell(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd  = OxmlElement("w:shd")
    shd.set(qn("w:val"),   "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"),  fill_hex)
    tcPr.append(shd)

def _cell_borders(cell, colour_hex, size):
    tcPr = cell._tc.get_or_add_tcPr()
    tcBorders = OxmlElement("w:tcBorders")
    for side in ("top", "left", "bottom", "right"):
        el = OxmlElement(f"w:{side}")
        el.set(qn("w:val"),   "single")
        el.set(qn("w:sz"),    str(size))
        el.set(qn("w:color"), colour_hex)
        tcBorders.append(el)
    tcPr.append(tcBorders)

def _cell_width(cell, cm_val):
    tcPr = cell._tc.get_or_add_tcPr()
    tcW  = OxmlElement("w:tcW")
    tcW.set(qn("w:w"),    str(_twips(cm_val)))
    tcW.set(qn("w:type"), "dxa")
    tcPr.append(tcW)

def _header_cell(cell, text, width):
    cell.text = ""
    _shade_cell(cell, NAVY_HEX)
    _cell_borders(cell, BLUE_HEX, 6)
    _cell_width(cell, width)
    p = cell.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    _add_run(p, text, size=9, bold=True, colour=WHITE)

def _data_cell(cell, text, width, fill=WHITE_HEX):
    cell.text = ""
    _shade_cell(cell, fill)
    _cell_borders(cell, CC_HEX, 4)
    _cell_width(cell, width)
    p = cell.paragraphs[0]
    _add_run(p, text or "", size=9, colour=GREY)

def _summary_row(table, col_widths, label_text, value_text, label_fill, label_colour_hex, bold_label=False):
    row   = table.add_row()
    cells = row.cells
    # Merge first 4 cells for label
    merged = cells[0].merge(cells[1]).merge(cells[2]).merge(cells[3])
    _shade_cell(merged, label_fill)
    _cell_borders(merged, BLUE_HEX, 6)
    p = merged.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    lc = WHITE if label_fill == NAVY_HEX else NAVY
    _add_run(p, label_text, size=10, bold=bold_label, colour=lc)

    vc = cells[4]
    _shade_cell(vc, label_fill)
    _cell_borders(vc, BLUE_HEX, 6)
    _cell_width(vc, col_widths[4])
    vp = vc.paragraphs[0]
    vc_text_colour = WHITE if label_fill == NAVY_HEX else GREY
    _add_run(vp, value_text, size=10, bold=bold_label, colour=vc_text_colour)

def _sig_header_cell(cell, text, width):
    _cell_width(cell, width)
    tcPr = cell._tc.get_or_add_tcPr()
    tcBorders = OxmlElement("w:tcBorders")
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"),   "single")
    bottom.set(qn("w:sz"),    "6")
    bottom.set(qn("w:color"), NAVY_HEX)
    tcBorders.append(bottom)
    tcPr.append(tcBorders)
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(40)
    _add_run(p, text, size=9, bold=True, colour=NAVY)
