# -*- coding:utf-8 _*-

import openai

from bot.config import openai_api_key


def generate_text(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=60,
        n=1,
        stop=None,
        temperature=0.5,
    )
    text = response.choices[0].text
    return text.strip()


if __name__ == '__main__':
    openai.api_key = openai_api_key
    prompt = "在一个阳光明媚的早晨，一个年轻人走进了一家咖啡店。"
    generated_text = generate_text(prompt)
    print(generated_text)
