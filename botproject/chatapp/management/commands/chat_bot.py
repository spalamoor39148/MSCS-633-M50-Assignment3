"""Custom Django management command that starts a terminal chatbot."""
from __future__ import annotations

from django.core.management.base import BaseCommand

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


class Command(BaseCommand):
    help = 'Start a terminal chat session with the trained ChatterBot bot.'

    def handle(self, *args, **options) -> None:
        bot = ChatBot(
            'AssignmentBot',
            storage_adapter='chatterbot.storage.SQLStorageAdapter',
            database_uri='sqlite:///db.sqlite3',
            logic_adapters=[
                {
                    'import_path': 'chatterbot.logic.BestMatch',
                    'default_response': 'I am still learning. Could you rephrase that?',
                    'maximum_similarity_threshold': 0.90,
                }
            ],
        )

        trainer = ListTrainer(bot)
        trainer.train(
            [
                'Good morning! How are you doing?',
                'I am doing very well, thank you for asking.',
                "You're welcome.",
                'Do you like hats?',
                'What is your name?',
                'My name is AssignmentBot.',
                'Bye',
                'Goodbye! Have a great day.',
            ]
        )

        self.stdout.write(self.style.SUCCESS("Chat started. Type 'exit' or 'quit' to stop.\n"))

        while True:
            user_text = input('user: ').strip()
            if user_text.lower() in {'exit', 'quit'}:
                self.stdout.write('bot: Goodbye! Have a great day.')
                break

            reply = bot.get_response(user_text)
            self.stdout.write(f'bot: {reply}')
