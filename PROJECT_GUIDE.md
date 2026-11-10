
# 🔐 PrivacyCheck

## About the Project

PrivacyCheck is a Python-based privacy protection tool designed to identify sensitive information in text before it is shared online.

## Features

- Email address detection
- Phone number detection
- URL detection
- Possible password detection
- Sensitive information masking
- Privacy risk scoring
- Automated testing
- Streamlit user interface

## Technologies Used

- Python
- Regular Expressions
- Streamlit
- Pytest
- GitHub

## Project Structure

PrivacyCheck/
│
├── README.md
├── requirements.txt
├── detector.py
├── scanner.py
├── privacy_app.py
├── text_input.py
├── scan_results.py
├── privacy_score.py
├── test_privacy.py
└── PROJECT_GUIDE.md

## Installation

Install dependencies:

pip install -r requirements.txt

## Run the Application

streamlit run privacy_app.py

## Run Tests

pytest -v

## Project Objective

To help users identify and protect personal information before sharing content publicly.

## Future Improvements

- Better password detection
- More accurate phone number validation
- File scanning support
- Downloadable privacy reports
- Improved user interface

## Author

Created as a Python learning project.

## Status

Initial development completed.
