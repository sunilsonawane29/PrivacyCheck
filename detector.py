
import re

def detect_emails(text):
    """
    Detect email addresses in a given text.
    """
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'

    emails = re.findall(pattern, text)

    return emails
