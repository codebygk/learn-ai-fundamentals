## Chat Completions
- Create a `.env` file at the root of the directory.
- Add `OPENAI_API_KEY` variable in the environment file like below.
  ```
  OPENAI_API_KEY=sk-proj-XXXXXXXXXXXXXXXXXXXXXXXXXXXX
  ```

  Note: Replace _sk-proj-XXXXXXXXXXXXXXXXXXXXXXXXXXXX_ with your own key copied from [Setup OpenAI](./06-Setup-OpenAI.md)


### With Requests
```python
import requests
headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}

payload = {
    "models": "gpt-5-nano",
    "messages": [
        {"role": "user", "content": "Tell me a fun fact"}
    ]
}

response = requests.post(
    "https://api.openai.com/v1/chat/completions", 
    headers=headers,
    json=payload
)
content = response.json()["choices"][0]["messages"]["content"]
print(content)
```


### With OpenAI Package
```python
from openai import OpenAI

openai = OpenAI()

response = openai.chat.completions.create(
    model="gpt-5-nano",
    messages=[
        {
            "role": "user", 
            "content": "Tell me a fun fact"
        }
    ]
)
content = response.choices[0].message.content
print(content)
```

---

Previous: [Models](/08-models.md) | Next: [Transformers](/10-transformers.md)