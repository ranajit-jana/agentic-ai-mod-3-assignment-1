# Setup and Run Instructions

This document explains how to install dependencies and run the Legal Document Review Application locally.

## Requirements

- Python 3.12+
- pip package manager
- Google Gemini API key

## Install Dependencies

1. Create and activate a virtual environment:
   ```bash
   python3.12 -m venv venv
   source venv/bin/activate
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Configure API Key

1. Create a .env file

2. Open `.env` and add your Google Gemini API key:
   ```bash
   GOOGLE_API_KEY=your_api_key_here
   ```

## Run the Application

Start the Streamlit app:
```bash
streamlit run app.py
```

Then open the app in your browser:

- `http://localhost:8501`

## What to Do Next

- Upload a legal PDF document
- Review extracted text and document preview
- Ask questions about the document
- Generate a concise document summary

## Notes

- Make sure `.env` is present before running the app
- The application reads the API key from `GOOGLE_API_KEY` in the `.env` file
- If you update dependencies, rerun `pip install -r requirements.txt`
