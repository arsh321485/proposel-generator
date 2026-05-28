# SecureITLab Proposal Generator — Backend Setup Guide

## Project Structure

```
secureitlab_backend/
├── main.py                              ← FastAPI backend (this is what you run)
├── proposal_data.py                     ← All 57 service methodology + timeline data
├── SecureITLab_Proposal_Generator.html  ← Updated front-end (calls the backend)
├── requirements.txt                     ← Python dependencies
└── README.md                            ← This file
```

---

## How It Works

```
Browser (HTML form)
       │  fills in form, clicks Generate
       ▼
POST /generate  ──→  FastAPI (main.py)
                           │  looks up proposal_data.py
                           │  builds the .docx in memory
                           ▼
                     Returns .docx file
       │
       ▼
Browser downloads the file automatically
```

---

## Step 1 — Install Python Dependencies

You need **Python 3.9+**. Open a terminal in the project folder and run:

```bash
pip install -r requirements.txt
```

This installs:
- `fastapi` — the web framework
- `uvicorn` — the server that runs FastAPI
- `python-docx` — builds the Word document
- `pydantic` — validates the form data
- `lxml` — XML handling for docx

---

## Step 2 — Run the Backend

```bash
uvicorn main:app --reload --port 8000
```

You should see:

```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process
```

Leave this terminal running. The `--reload` flag auto-restarts the server when you edit code.

---

## Step 3 — Open the Front-End

Open `SecureITLab_Proposal_Generator.html` directly in your browser:

```
File → Open → SecureITLab_Proposal_Generator.html
```

Or double-click the file. The form will load. When you click **Generate & Download Proposal**, it will:

1. Collect all form data
2. Send it to `http://localhost:8000/generate`
3. Download the `.docx` file automatically

---

## API Endpoints

| Method | URL | Description |
|--------|-----|-------------|
| `GET`  | `/` | Serves the HTML front-end |
| `GET`  | `/services` | Lists all 57 service keys |
| `GET`  | `/services/{key}` | Returns methodology + timeline for a service |
| `POST` | `/generate` | Accepts form data, returns `.docx` file |

You can test the API in your browser at: **http://localhost:8000/docs**  
(FastAPI auto-generates interactive API documentation)

---

## Troubleshooting

### "Error: Failed to fetch" in the browser
The backend is not running. Make sure you ran `uvicorn main:app --reload --port 8000` and the terminal shows no errors.

### "CORS error" in the browser console
This happens if you open the HTML from a different server. Open the file directly in the browser (File → Open), or run both from the same origin.

### "Service key not found"
The service selected in the form doesn't match a key in `proposal_data.py`. Check that all 57 keys are present.

### Port already in use
```bash
uvicorn main:app --reload --port 8001   # use a different port
```
Then update line 2 of `SecureITLab_Proposal_Generator.html`:
```javascript
const API_BASE = 'http://localhost:8001';
```

---

## Deploying to a Server (Optional)

If you want to run this on a server so your team can access it from any browser:

### 1. Upload all files to the server

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run with a process manager (so it stays running)
```bash
pip install gunicorn
gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

### 4. Update API_BASE in the HTML
Change line 2 of `SecureITLab_Proposal_Generator.html`:
```javascript
const API_BASE = 'https://your-server-domain.com';
```

### 5. (Recommended) Add Nginx as a reverse proxy and HTTPS

---

## Updating Proposal Content

All methodology text and timeline data lives in `proposal_data.py`. To update a service:

1. Open `proposal_data.py`
2. Find the key (e.g. `"Penetration_Testing"`)
3. Edit the `methodology` list or `timeline` tuples
4. Save — the backend picks up changes immediately (with `--reload`)

No changes needed to the HTML or `main.py`.
