# echo_model.py
# Author: Nikita Lemeshenko


class EchoModel:
    """A model that repeats the last message."""

    def reply(self, instructions, history):
        last_message = history[-1]["content"]
        return f"You said: {last_message}"
