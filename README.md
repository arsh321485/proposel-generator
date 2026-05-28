# SecureITLab Proposal Generator — Setup Guide

## Project Structure

```
files (1)\
├── main.py                              ← FastAPI backend (run this)
├── proposal_data.py                     ← All 57 service methodology + timeline data
├── SecureITLab_Proposal_Generator.html  ← Frontend (served automatically)
├── requirements.txt                     ← Python dependencies
├── downloads.csv                        ← Auto-created when first proposal is generated
└── README.md                            ← This file
```

---

## How It Works

```
Browser → http://127.0.0.1:8000
              │
              ▼
        FastAPI (main.py)
              │
              ├── Serves the frontend HTML automatically
              │
              ├── POST /generate → builds .docx → downloads to browser
              │                  → logs to downloads.csv automatically
              │
              └── GET /dashboard → admin login → shows download tracking
```

---

## Step 1 — Install Python Dependencies

You need **Python 3.12**. Open terminal in the project folder and run:

```bash
py -3.12 -m pip install -r requirements.txt
```

Only needed once.

---

## Step 2 — Run the Backend

```bash
py -3.12 -m uvicorn main:app --reload --port 8000
```

You should see:
```
INFO:     Uvicorn running on http://127.0.0.1:8000
INFO:     Application startup complete.
```

Leave this terminal running.

---

## Step 3 — Open the Frontend

Open your browser and go to:
```
http://127.0.0.1:8000
```

The proposal form loads automatically. No need to open the HTML file manually.

---

## Step 4 — Open the Admin Dashboard

Open your browser and go to:
```
http://127.0.0.1:8000/dashboard
```

Enter your login:

| Field    | Default Value      |
|----------|--------------------|
| Username | `admin`            |
| Password | `secureitlab2024`  |

### Dashboard Shows:
- Total downloads (all time)
- Downloads today
- Unique clients and services
- Full download log table (searchable)
- Top 5 most used services
- Export button to download CSV

---

## Step 5 — Export the CSV

**Option A — From the dashboard:**
Click the **⬇ Export CSV** button on the dashboard.

**Option B — From the folder:**
Open `downloads.csv` directly in Excel.
Located at:
```
C:\Users\DELL\Downloads\files (1)\downloads.csv
```

### CSV Columns:
| Column | Description |
|---|---|
| Timestamp | Date and time of download |
| Client Name | Primary contact name |
| Organisation | Company name |
| Service | Service selected |
| Reference | Proposal reference number |
| IP Address | IP of the person who downloaded |
| Filename | Name of the downloaded .docx file |

---


## API Endpoints

| Method | URL | Description |
|--------|-----|-------------|
| `GET`  | `/` | Serves the frontend form |
| `GET`  | `/services` | Lists all 57 service keys |
| `GET`  | `/services/{key}` | Returns methodology + timeline for a service |
| `POST` | `/generate` | Accepts form data, returns `.docx`, logs download |
| `GET`  | `/dashboard` | Admin dashboard (login required) |
| `GET`  | `/dashboard/export` | Downloads full CSV (login required) |

Interactive API docs available at: **http://127.0.0.1:8000/docs**


## Troubleshooting

### Frontend not loading at http://127.0.0.1:8000
Make sure `SecureITLab_Proposal_Generator.html` is in the same folder as `main.py`.

### "Failed to fetch" error when generating
Backend is not running. Run the uvicorn command again.

### Port already in use
```bash
py -3.12 -m uvicorn main:app --reload --port 8001
```
Then update line 2 of `SecureITLab_Proposal_Generator.html`:
```javascript
const API_BASE = 'http://localhost:8001';
```

### downloads.csv not appearing
Generate at least one proposal first — the file is created automatically on first download.

### Module not found error
Run the install command again:
```bash
py -3.12 -m pip install -r requirements.txt
```

---

## Updating Proposal Content

All methodology and timeline data is in `proposal_data.py`.

1. Open `proposal_data.py`
2. Find the service key (e.g. `"Penetration_Testing"`)
3. Edit the `methodology` list or `timeline` tuples
4. Save — backend picks up changes automatically

No changes needed to `main.py` or the HTML file.

---

## Daily Usage (Quick Reference)

```
1. Open terminal in project folder
2. Run: py -3.12 -m uvicorn main:app --reload --port 8000
3. Frontend → http://127.0.0.1:8000
4. Dashboard → http://127.0.0.1:8000/dashboard
```

---

*SecureITLab — Cybersecurity | Data Privacy | Data Governance*