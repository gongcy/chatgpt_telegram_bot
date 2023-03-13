# ChatGPT Telegram Bot: **Fast. No daily limits. Special chat modes**

<div align="center">
<img src="./static/header.png" align="center" style="width: 100%" />
</div>

We all love [chat.openai.com](https://chat.openai.com), but... It's TERRIBLY laggy, has daily limits, and is only accessible through an archaic web interface.

This repo is ChatGPT re-created with GPT-3.5 LLM as Telegram Bot. **And it works great.**

You can deploy your own bot, or use mine: [@chatgpt_karfly_bot](https://t.me/chatgpt_karfly_bot)

## News
- *9 Mar 2023*: Now you can easily create your own Chat Modes by editing `config/chat_modes.yml`
- *8 Mar 2023*: Added voice message recognition with [OpenAI Whisper API](https://openai.com/blog/introducing-chatgpt-and-whisper-apis). Record a voice message and ChatGPT will answer you!
- *2 Mar 2023*: Added support of [ChatGPT API](https://platform.openai.com/docs/guides/chat/introduction). It's enabled by default and can be disabled with `use_chatgpt_api` option in config. Don't forget to **rebuild** you docker image (`--build`).

## Features
- Low latency replies (it usually takes about 3-5 seconds)
- No request limits
- Voice message recognition
- Code highlighting
- Special chat modes: 👩🏼‍🎓 Assistant, 👩🏼‍💻 Code Assistant, 📝 Text Improver and 🎬 Movie Expert. You can easily create your own chat modes by editing `config/chat_modes.yml`
- Support of [ChatGPT API](https://platform.openai.com/docs/guides/chat/introduction)
- List of allowed Telegram users
- Track $ balance spent on OpenAI API

## Bot commands
- `/retry` – Regenerate last bot answer
- `/new` – Start new dialog
- `/mode` – Select chat mode
- `/balance` – Show balance
- `/help` – Show help

## Setup
1. Get your [OpenAI API](https://openai.com/api/) key

2. Get your Telegram bot token from [@BotFather](https://t.me/BotFather)

3. Edit `config/config.example.yml` to set your tokens and run 2 commands below (*if you're advanced user, you can also edit* `config/config.example.env`):
```bash
mv config/config.example.yml config/config.yml
mv config/config.example.env config/config.env
```

🔥 And now **run**:

```bash
docker-compose --env-file config/config.env up --build
```


## Configure command hints (optional, but fancy)

At [@BotFather](https://t.me/BotFather), use command `/mybots` -> select your bot -> Edit Bot -> Edit Commands. Then paste the following text to the BotFather:

```
retry - Regenerate last bot answer
new - Start new dialog
mode - Select chat mode
balance - Show balance
help - Show help
```

After that, you will be able to utilize menu shortcuts or receive prompts while entering commands.

## References
1. [*Build ChatGPT from GPT-3*](https://learnprompting.org/docs/applied_prompting/build_chatgpt)
