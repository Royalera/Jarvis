import webbrowser
import requests

# List of common domain extensions
domains = [".com", ".org", ".edu", ".gov", ".net", ".int", ".mil"]

# Headers for making requests
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
}

def check_url_status(website):
    """Check if a website with common domains is accessible."""
    for domain in domains:
        full_url = f"https://www.{website}{domain}"
        try:
            response = requests.get(full_url, headers=headers, timeout=5)
            if response.status_code == 200:
                return True, full_url
        except requests.RequestException:
            continue  # Skip to the next domain if request fails
    return False, None

def open_url(website):
    """Try to open a website in a browser."""
    status, valid_url = check_url_status(website)
    if status:
        webbrowser.open(valid_url)
        return True
    return False
