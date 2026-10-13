from dotenv import load_dotenv
from openai import OpenAI
import os
import gradio as gr
import truststore

truststore.inject_into_ssl()



load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
if not api_key:
    raise ValueError("OPENAI_API_KEY is not found in environment variables")
client = OpenAI(api_key=api_key)


MODEL = "gpt-4o-mini"
SYSTEM_PROMPT = open("prompt.txt", encoding="utf-8").read()



def respond(message, history):
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    for msg in history:
        messages.append({"role": msg["role"], "content": msg["content"]})
    messages.append({"role": "user", "content": message})

    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
    )
    return response.choices[0].message.content


def main():
    gr.ChatInterface(fn=respond).launch()

#     text = input("> ")
#     print(get_command(text))


if __name__ == "__main__":
    main()
