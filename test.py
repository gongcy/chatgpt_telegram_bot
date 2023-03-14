# -*- coding:utf-8 _*-

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


if __name__ == '__main__':
    prompt = "在一个阳光明媚的早晨，一个年轻人走进了一家咖啡店。"
    generated_text = generate_text(prompt)
    print(generated_text)
