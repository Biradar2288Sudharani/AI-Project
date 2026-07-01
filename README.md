# 🏥 DScribe AI – Hospital Discharge Summary Generator
An AI-assisted healthcare application that extracts important clinical information from hospital PDF documents and automatically 
generates a structured discharge summary.
This project was developed using **Python**, **Flask**, **PyMuPDF**, **OCR (Tesseract)**, and a modular Agent architecture to automate 
the extraction of patient information from clinical records.
---
# 📌 Project Overview
Hospital discharge documents often contain multiple pages of medical records such as:
- Admission Notes
- Nursing Notes
- Observation Charts
- Medication Records
- Investigation Reports
- Procedure Notes
- Discharge Checklist
Reading these documents manually is time-consuming.
This project reads uploaded PDF files, extracts important medical information, validates missing fields, and generates a discharge summary draft for clinician review.
---

# 🚀 Features
✅ Upload Hospital PDF Documents
✅ Read Digital PDF Files
✅ OCR Support for Scanned Pages
✅ Multi-page PDF Processing
✅ Automatic Document Classification

Supports identification of:
- Admission Notes
- Nursing Documentation
- Observation Charts
- Laboratory Reports
- Medication Records
- Procedure Documents
- Discharge Summary
---

# 🩺 Clinical Information Extraction
The system extracts important medical information including:
- Patient Name
- Admission Date
- Discharge Date
- Principal Diagnosis
- Secondary Diagnosis
- Hospital Course
- Procedures
- Allergies
- Discharge Medications
- Follow-up Instructions
- Discharge Condition
- Pending Results
---

# 🤖 Agent Workflow
The application follows an Agent-based workflow.
Step 1
Read uploaded PDF
↓
Step 2
Extract PDF text
↓
Step 3
Run OCR (if required)
↓
Step 4
Classify document type
↓
Step 5
Extract clinical information
↓
Step 6
Validate missing information
↓
Step 7
Medication reconciliation
↓
Step 8
Conflict detection
↓
Step 9
Drug interaction checking
↓
Step 10
Generate discharge summary
---
# 🛠 Technologies Used
### Backend
- Python
- Flask
### PDF Processing
- PyMuPDF (fitz)
- Tesseract OCR
- Pillow
### AI / Automation
- Rule-based Clinical Information Extraction
- Document Classification
- Agent Workflow
### Database
- MySQL (optional)
### API Testing
- Swagger UI
- Postman
---

# ⚙ Installation
Clone repository
```bash
git clone https://github.com/yourusername/dscribe-ai.git
```
Create virtual environment
```bash
python -m venv venv
```
Activate
Windows
```bash
venv\Scripts\activate
```
Install dependencies
```bash
pip install -r requirements.txt
```

