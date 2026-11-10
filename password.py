
import re

def detect_emails(text):
    """Detect email addresses in the given text."""
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
    return re.findall(pattern, text)


def detect_phones(text):
    """Detect possible phone numbers in the given text."""
    pattern = r'(?<!\w)(?:\+?\d{1,3}[-.\s]?)?\d{10}(?!\w)'
    return re.findall(pattern, text)


def detect_urls(text):
    """Detect HTTP, HTTPS, and www URLs."""
    pattern = r'https?://[^\s]+|www\.[^\s]+'
    return re.findall(pattern, text)


def detect_passwords(text):
    """Detect possible password assignments."""
    pattern = r'(?i)\b(password|passwd|pwd)\s*[:=]\s*[^\s,;]+'
    return re.findall(pattern, text)
