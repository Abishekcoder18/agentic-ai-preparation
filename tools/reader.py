import requests
from bs4 import BeautifulSoup


def fetch_webpage(url):
    """
    Fetch the text content of a webpage.

    Args:
        url (str): Webpage URL

    Returns:
        str: Extracted text, or empty string if failed
    """

    try:
        response = requests.get(url, timeout=10)

        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        paragraphs = soup.find_all("p")

        text = "\n".join(
            paragraph.get_text(strip=True)
            for paragraph in paragraphs
        )

        return text

    except Exception as e:
        print(f"Reader failed: {e}")
        return ""