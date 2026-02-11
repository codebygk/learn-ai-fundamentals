## LLM Frameworks

### Langchain
- Powerful but heavy llm framework

```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-5-mini")
response = llm.invoke(tell_a_joke)
print(response.content)
```


### LiteLLM
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


### Prompt Caching
