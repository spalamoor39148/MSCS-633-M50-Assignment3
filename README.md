# Django + ChatterBot Terminal Client

This project is a simple terminal chatbot built with Python, Django, and ChatterBot.

## Features
- Uses a Django custom management command for terminal chat
- Trains ChatterBot with a short sample conversation
- Stores the bot database in SQLite
- Uses comments and clear structure for readability

## Setup
```bash
python -m venv venv
source venv/bin/activate      # macOS/Linux
# venv\Scripts\activate      # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py chat_bot
```

## Example session
```text
user: Good morning! How are you doing?
bot: I am doing very well, thank you for asking.
user: You're welcome.
bot: Do you like hats?
```

## Suggested GitHub repo structure
- botproject/
  - manage.py
  - requirements.txt
  - README.md
  - botproject/
  - chatapp/

Upload this folder to GitHub and place your repository URL inside the Word document before submitting.
