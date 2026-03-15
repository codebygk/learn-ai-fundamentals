## Tokens
In LLMs (Large Language Models), tokens are the basic units of text that the model reads, processes, and generates. 
Tokens are how text is broken down before the model understands it.

## History of Tokens
- Initially, training the neural networks happened at the **character level**. This approach resulted in a very small vocab and required so much from the neural network to predict the next character.
- Then, training happened at the **word level**. This resulted in easier learning but needs to maintain a enormous vocab and rare words are omitted.
- Now, we have **tokens** which acts as a middleground between the above two approaches. In tokens approach, the models are trained on chunk of words which resulted in optimal vocab and better training efficiency. This approach is also efficient in handling word stems (share, shareable, etc.)

## Tokenization
- Splitting the words into chunks of tokens for better context understanding.

## Tools
- [GPT Tokenizer](https://platform.openai.com/tokenizer): Webapp to visualize how words are split into chunks in OpenAI models.
- [Tiktoken](https://pypi.org/project/tiktoken): Library to view tokenization for any model. It supports encoding and decoding of words.

## Tiktoken
```python
import tiktoken
encoding = tiktoken.encoding_for_model("gpt-oss")
tokens = encoding.encode("Hi, I love llm models")

for token_id in tokens:
    token_text = encoding.decode([token_id])
    print(f"{token_id}: {token_text}")

```

---

Previous: [Parameters](/11-parameters.md) | Next: [Context Windows](/13-context-windows.md)