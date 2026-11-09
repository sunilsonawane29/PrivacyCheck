
def detect_phone_numbers(text):
    """
    Detect possible phone numbers in text.
    """
    pattern = r'\b(?:\+?\d{1,3}[-.\s]?)?\d{10}\b'

    phone_numbers = re.findall(pattern, text)

    return phone_numbers
