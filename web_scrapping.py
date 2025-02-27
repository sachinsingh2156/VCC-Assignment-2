import threading
import requests
from bs4 import BeautifulSoup

# List of websites to scrape
websites = [
    "https://www.python.org",
    "https://www.wikipedia.org",
    "https://www.github.com",
    "https://www.stackoverflow.com",
    "https://www.nytimes.com"
]

def fetch_title(url):
    """Fetch the title of the webpage given its URL."""
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Raise exception for HTTP errors
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string.strip() if soup.title else "No Title Found"
        print(f"{url} --> {title}")
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")

# Creating multiple threads
threads = []
for website in websites:
    thread = threading.Thread(target=fetch_title, args=(website,))
    threads.append(thread)
    thread.start()

# Waiting for all threads to finish
for thread in threads:
    thread.join()

print("Web scraping completed successfully!")
