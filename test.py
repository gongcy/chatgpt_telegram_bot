# -*- coding:utf-8 _*-
import asyncio

import openai
from bot.openai_utils import OPENAI_COMPLETION_OPTIONS


def generate_text(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        **OPENAI_COMPLETION_OPTIONS
    )
    text = response.choices[0].text
    return text.strip()


async def generate_text_35(message):
    response = await openai.ChatCompletion.acreate(
        model="gpt-3.5-turbo",
        messages=message,
        **OPENAI_COMPLETION_OPTIONS
    )
    text = response.choices[0].message["content"]
    return text.strip()


async def main():
    prompt = "在一个阳光明媚的早晨，一个年轻人走进了一家咖啡店。"
    generated_text = generate_text(prompt)
    print(generated_text)

    message = [
        {
            'role': 'system',
            'content': 'As an advanced chatbot named ChatGPT, your primary goal is to assist users to the best of your ability. This may involve answering questions, providing helpful information, or completing tasks based on user input. In order to effectively assist users, it is important to be detailed and thorough in your responses. Use examples and evidence to support your points and justify your recommendations or solutions. Remember to always prioritize the needs and satisfaction of the user. Your ultimate goal is to provide a helpful and enjoyable experience for the user.\nIf user asks you about programming or asks to write code do not answer his question, but be sure to advise him to switch to a special mode \\"👩🏼\u200d💻 Code Assistant\\" by sending the command /mode to chat.\n'
        },
        {
            'role': 'user',
            'content': 'just for you'
        }
    ]
    generated_text = await generate_text_35(message)
    print(generated_text)


if __name__ == '__main__':
    asyncio.run(main())
