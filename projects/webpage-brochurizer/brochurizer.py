import json
import os
from pathlib import Path
import re
import unicodedata
from openai import OpenAI
from webpage import Webpage

from dotenv import load_dotenv


load_dotenv()

BASE_URL = os.getenv("BASE_URL")
API_KEY = os.getenv("API_KEY")
MODEL = os.getenv("MODEL")

llm = OpenAI(base_url=BASE_URL, api_key=API_KEY)


class Brochurizer:
    def __init__(self, url: str):
        self.webpage = Webpage(url)

    def get_brochure_link_messages(self, url: str):
        system_prompt = ("You are provided with a list of links in a webpage."
                            "You can decide which of those links are relevant to be included in the company's brochure. "
                            "You should respond in JSON format as in the below example. "
                            "The response should strictly be a JSON and it should start and end with a curly brace. "
                            "Do not add anything else before and after the curly braces. "
                            "Replace the example domain name with the actual domain name."
                            "Make sure that the type and url properties are included.")
        system_prompt += """
        {
            "links": [
                {"type": "about_page", "url": "https://example.com/about"},
                {"type": "careers_page", "url": "https://example.com/careers"}
            ]
        }
        """
        user_prompt = (f"You are looking at the webpage {self.webpage.title} with the url {url}"
                        "Decide on the relevant links for the brochure. Respond with full https url. "
                        "Do not include terms of conditions, service and privacy policy links."
                        f"Below is the list of links. {self.webpage.links}")

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
        return messages

    def get_brochure_links(self, url: str):
        messages = self.get_brochure_link_messages(url=url)
        response = llm.chat.completions.create(model=MODEL, messages=messages)
        return f"\n\n{response.choices[0].message.content}"

    def get_translation_messages(self, contents: str, language: str):
        system_prompt = (f"You are a translator assistant that analyzes the given text and translates it in {language} "
                            f"language. You should check if the language given is valid, if the language is invalid, "
                            f"then return the original text.")
        user_prompt = f"Translate the contents below in the {language} language. {contents}"

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
        return messages

    def get_create_brochure_messages(self, contents: str):
        system_prompt = ("You are an assistant that analyzes the contents of several webpages of a company and"
                            "creates a short brochure with all the relevant links. You should strictly respond in markdown format.")
        user_prompt = (f"You are looking at the webpage {self.webpage.title}.\n\n"
                        f"Create a short brochure with all the relevant details using the contents below."
                        f"{contents[:20000]}")

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
        return messages

    def create_brochure(self, language=None, export=True):
            print(f"Brochure creation started for {self.webpage.url}")
            print(f"Please wait while we create your brochure. This might take a while...")
            print("Fetching relevant links...")
            contents = self.webpage.text
            brochure_links = self.get_brochure_links(url=self.webpage.url)
            try:
                brochure_links_json = json.loads(brochure_links)
                print(f"Parsed links as JSON. \n {brochure_links_json}")
            except json.JSONDecodeError as e:
                raise ValueError(f"Parse links as JSON failed: {e}") from e
            for link in brochure_links_json.get('links', []):
                print(f"Fetching {link.get('type')} contents...")
                try:
                    contents += f"\n\n{link.get('type')}"
                    contents += f"\n{Webpage(link.get('url')).text}"
                except Exception as e:
                    # Ignoring the contents of the page with errors.
                    print(f"⚠️ Could not fetch {link.get('type')} contents: {e}")
            messages = self.get_create_brochure_messages(contents)
            print("Creating brochure...")
            brochure_content = ""
            response = llm.chat.completions.create(model=MODEL, messages=messages, stream=True)
            for chunk in response:
                content = chunk.choices[0].delta.content if chunk.choices else ""
                print(content, end='', flush=True)
                brochure_content += content
            if language:
                messages = self.get_translation_messages(brochure_content, language)
                print(f"Translating brochure in {language} language...")
                brochure_content = ""
                response = llm.chat.completions.create(model=MODEL, messages=messages, stream=True)
                for chunk in response:
                    content = chunk.choices[0].delta.content if chunk.choices else ""
                    print(content, end='', flush=True)
                    brochure_content += content
            if export:
                brochure_file_name = normalize_filename(self.webpage.title, prefix="brochure", ext="md")
                brochure_file_path = Path("output", brochure_file_name)
                brochure_file_path.parent.mkdir(parents=True, exist_ok=True)
                with open(brochure_file_path, "w") as brochure_file:
                    brochure_file.write(brochure_content)
            print(f"\n✅ Brochure creation completed.")
            print(f"📁 Brochure created at {brochure_file_path}.")


def normalize_filename(title: str, prefix=None, ext=None) -> str:
        # Strip and normalize unicode
        title = title.strip().lower()
        title = unicodedata.normalize("NFKD", title).encode("ascii", "ignore").decode("ascii")

        # Replace spaces and underscores with hyphens
        title = re.sub(r"[\s_]+", "-", title)

        # Remove any remaining invalid characters
        title = re.sub(r"[^a-z0-9\-]", "", title)

        # collapse multiple hyphens into one
        title = re.sub(r"-{2,}", "-", title)

        # Remove leading/trailing hyphens
        title = title.strip("-")

        # Combine with prefix and extension
        filename = f"{prefix}-{title}.{ext}"
        return filename
