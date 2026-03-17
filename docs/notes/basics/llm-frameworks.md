# LLM Frameworks

## Langchain
- Powerful but heavy llm framework

```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-5-mini")
response = llm.invoke(tell_a_joke)
print(response.content)
```


## LiteLLM
- Lightweight llm framework

```python
response = completion(model=MODEL, messages=messages)
response_content = response.choices[0].message.content
print(response_content)

print(f"Input Tokens: {response.usage.prompt_tokens}")
print(f"Output Tokens: {response.usage.completion_tokens}")
print(f"Total Tokens: {response.usage.total_tokens}")
print(f"Total Cost: {response._hidden_params["response_cost"]*100:.4f} cents")
```


## Prompt Caching
- Cache allows users to reduce upto 10x costs but need to pay small additional cost for enabling prompt caching.

```python

with open("files/shakespeare.txt", "r", encoding="utf-8") as f:
    shakespeare = f.read()

loc = shakespeare.find("what answer made the belly?")
print(shakespeare[loc:loc+100])


question = [{"role": "user", "content": "In shakespeare text, when a citizen asked 'what answer made the belly? what is the reply from MENENIUS" }]
response = completion(model="ollama/gpt-oss", messages=question)
print(response.choices[0].message.content)

print(f"Input Tokens: {response.usage.prompt_tokens}")
print(f"Output Tokens: {response.usage.completion_tokens}")
print(f"Total Tokens: {response.usage.total_tokens}")
print(f"Total Cost: {response._hidden_params["response_cost"]*100:.4f} cents")
```
!!! note
    Always add the questions or variable text at the end, to effectively enable cache as the initial text will remain the same in all requests.
    
