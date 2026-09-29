# LegalEase: AI-Powered Legal Document Generator

LegalEase uses Generative AI to simplify the creation of legal documents. Users can generate employment contracts, lease agreements, NDAs, and more — all tailored to their inputs and downloadable as PDF, DOCX, or TXT.

## Features

- AI Document Generation using Google Gemini
- Editable Preview before download
- Multi-Format Export: TXT, DOCX, PDF
- Interactive Streamlit UI
- REST API backend with FastAPI

## Tech Stack

- Backend: FastAPI, Python
- Frontend: Streamlit
- AI: Google Gemini (gemini-3.8-flash)
- Document Processing: python-docx, fpdf2

## How to Run Locally

### 1. Clone the repository

    git clone https://github.com/luci/2.0LegalEase.git
    cd 2.0LegalEase

### 2. Create and activate a virtual environment

    python -m venv venv
    venv\Scripts\activate

### 3. Install dependencies

    python -m pip install -r requirements.txt

### 4. Create a .env file

Add your Google Gemini API key:

    GEMINI_API_KEY=AIzaSyYourActualKeyHere

### 5. Start the FastAPI backend (Terminal 1)

    python -m uvicorn legalEaseAPI.main:app --reload

### 6. Start the Streamlit frontend (Terminal 2)

    python -m streamlit run frontend/app.py

### 7. Open in your browser

    http://localhost:8501

## Project Structure

    2.0LegalEase/
    ├── 1. Brainstorming & Ideation/
    ├── 2. Requirement Analysis/
    ├── 3. Project Design Phase/
    ├── 4. Project Planning Phase/
    ├── 5. Project Development Phase/
    ├── 6. Project Testing/
    ├── 7. Project Documentation/
    ├── 8. Project Demonstration/
    ├── ai_core/
    │   ├── __init__.py
    │   └── gemini_generator.py
    ├── legalEaseAPI/
    │   ├── __init__.py
    │   ├── main.py
    │   └── routes.py
    ├── frontend/
    │   └── app.py
    ├── .env
    ├── .gitignore
    ├── config.py
    ├── requirements.txt
    └── README.md