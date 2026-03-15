import os
from openai import OpenAI
from dotenv import load_dotenv

from webpage import Webpage


load_dotenv()

BASE_URL = os.getenv("BASE_URL")
API_KEY = os.getenv("API_KEY")
MODEL = os.getenv("MODEL")

llm = OpenAI(base_url=BASE_URL, api_key=API_KEY)

class Summarizer:
    def __init__(self, url: str):
        self.webpage = Webpage(url)


    def summarize(self):
        text = self.webpage.text
        system_prompt = ("You are an assistant that analyzes the text and provides a short summary, "
                        "ignoring text that might be navigation related. Respond in markdown.")
        user_prompt = (f"You should provide a short summary of this content in markdown. "
                        f"If it includes news or announcements, then summarize these too. "
                        f"The contents to be summarized given as below. {text}")
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
        print(f"Please wait while {MODEL} summarizes the webpage. This might take a while...")
        response = llm.chat.completions.create(model=MODEL, messages=messages)
        print(f"\n\n{response.choices[0].message.content}")
        print(f"Summarized the webpage {self.webpage.url}.")