
def detect_passwords(text):
    """
    Detect possible password assignments in text.
    """
    pattern = r'(?i)(?:password|passwd|pwd)\s*[:=]\s*[^\s,;]+'

    passwords = re.findall(pattern, text)

    return passwords
