from bs4 import BeautifulSoup
import requests


class Webpage:
    def __init__(self, url: str):
        self.url = url
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        self.title = soup.title.text if soup.title else "Untitled"
        irrelevant_tags = ["script", "style", "img", "input"]
        for tag in soup.body(irrelevant_tags):
            tag.decompose()
        self.text = soup.body.get_text(strip=True)
        self.links = [link.get('href') for link in soup.find_all('a')]
