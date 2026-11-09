
def detect_urls(text):
    """
    Detect URLs in a given text.
    """
    pattern = r'https?://[^\s]+|www\.[^\s]+'

    urls = re.findall(pattern, text)

    return urls
