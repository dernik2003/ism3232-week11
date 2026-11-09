# my_assistant.py
# Author: Nikita Lemeshenko

HANDOFF_WORDS = ["book", "schedule", "cancel", "payment"]


class RepairAssistant:
    """A bike shop assistant that uses a tool and an AI model."""

    def __init__(self, name, instructions, price_tool, model):
        self.name = name
        self.instructions = instructions
        self.price_tool = price_tool
        self.model = model
        self.history = []

    def respond(self, user_message):
        self.history.append({"role": "user", "content": user_message})

        reply = self.choose_reply(user_message)

        self.history.append({"role": "assistant", "content": reply})
        return reply

    def choose_reply(self, user_message):
        text = user_message.lower()

        if self.needs_human(text):
            return "I can't make changes to appointments. Please speak to an employee."

        if "price" in text or "cost" in text or "how much" in text:
            return self.price_reply(user_message)

        return self.model_reply()

    def needs_human(self, text):
        for word in HANDOFF_WORDS:
            if word in text:
                return True
        return False

    def price_reply(self, user_message):
        service = self.price_tool.find_service(user_message)

        if service is None:
            return "Which service? I can check flat tire, brake adjustment, or chain replacement."

        price = self.price_tool.price_for(service)

        if price is None:
            return "Sorry, I don't have a price for that service."

        return f"The price for {service} is ${price}."

    def model_reply(self):
        reply = self.model.reply(self.instructions, self.history)

        if reply is None:
            return "Sorry, I can't answer that right now. Please ask an employee."

        return reply
