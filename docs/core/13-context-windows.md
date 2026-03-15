## Context Windows
- Maximum number of tokens that the model can consider when generating the next token.
- Context window is the key to decide how well a model can remember the context.

**Note:** Every call to LLM is stateless. We need to pass the entire conversation in the input prompt everytime, instead of just the current one. This gives the illusion of and LLM having a memory.


## API Costs
- Chat interfaces have pro and monthly subscriptions. These are rate-limited but no per api call costs.
- APIs do not have subscriptions but charge per API call.
- The cost is based on the whole context including the input, output and follow-up questions. The whole chat is stacked up, sent and received with every api call to maintain context.

To view live api costs of all models, visit [LLM Leaderboard](https://vellum.ai/llm-leaderboard)

---

Previous: [Tokens](/12-tokens.md)