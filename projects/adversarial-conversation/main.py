
import os
from dotenv import load_dotenv
from openai import OpenAI

from config import load_agent_config

load_dotenv()


BASE_URL = os.getenv("BASE_URL")
API_KEY = os.getenv("API_KEY")
agent1 = load_agent_config("AGENT1")
agent2 = load_agent_config("AGENT2")

llm = OpenAI(base_url=BASE_URL, api_key=API_KEY)

def call_model1():
    model1_system_message = f'You are a chatbot who speaks in short sentences in {agent1.tone} tone.'
    messages = [{"role": "system", "content": model1_system_message}]
    for model1_message, model2_message in zip(model1_messages, model2_messages):
        messages.append({"role": "assistant", "content": model1_message})
        messages.append({"role": "user", "content": model2_message})
    response = llm.chat.completions.create(model=agent1.model, messages=messages, stream=True)
    print(f"\n{agent1.name}: ", end="")
    response_content = f""
    for chunk in response:
        content = chunk.choices[0].delta.content if chunk.choices else ""
        print(content, end="", flush=True)
        response_content += content
    return response_content

def call_model2():
    model2_system_message = f'You are a chatbot who speaks in short sentences in {agent2.tone} tone.'
    messages = [{"role": "system", "content": model2_system_message}]
    for model1_message, model2_message in zip(model1_messages, model2_messages):
        messages.append({"role": "user", "content": model1_message})
        messages.append({"role": "assistant", "content": model2_message})
    messages.append({"role": "user", "content": model1_messages[-1]})
    response = llm.chat.completions.create(model=agent2.model, messages=messages, stream=True)
    response_content = ""
    print(f"\n{agent2.name}: ", end="")
    for chunk in response:
        content = chunk.choices[0].delta.content if chunk.choices else ""
        print(content, end="", flush=True)
        response_content += content
    return response_content


def main():

    for i in range(5):
        model1_next = call_model1()
        model1_messages.append(model1_next)
        model2_next = call_model2()
        model2_messages.append(model2_next)


if __name__ == "__main__":
    model1_messages = ['Hi there!']
    model2_messages = ['Hi!']
    print(f'{agent1.name}: {model1_messages[0]}')
    print(f'{agent2.name}: {model2_messages[0]}')
    main()
