

import os
from dotenv import load_dotenv
from openai import OpenAI
from litellm import completion

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
API_KEY = os.getenv("API_KEY")
MODEL = os.getenv("MODEL")

llm = OpenAI(base_url=BASE_URL, api_key=API_KEY)


class Joker:
    def __init__(self, topic: str):
        self.topic = topic

    def tell_a_joke(self):
        system_prompt = (f"You are a joke teller assistant that tells jokes about {self.topic}. "
                            f"Make sure the joke is appropriate and funny.")
        user_prompt = f"Tell me a joke about {self.topic}"

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
        response = llm.chat.completions.create(model=MODEL, messages=messages, stream=True)
        joke_content = ""
        for chunk in response:
            content = chunk.choices[0].delta.content if chunk.choices else ""
            print(content, end='', flush=True)
            joke_content += content