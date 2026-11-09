# my_main.py
# Author: Nikita Lemeshenko

from my_assistant import RepairAssistant
from my_tool import RepairPriceTool
from ollama_model import OllamaModel

MODEL_NAME = "granite4.1:3b"

INSTRUCTIONS = """You are Jamie, a customer service assistant for Bayside Bike Repair.
Answer questions in one short sentence.
The shop is open Monday through Saturday from 9 am to 6 pm.
Simple repairs usually take 2 business days.
Only state facts that appear in these instructions.
If you do not know the answer, say so and suggest asking an employee."""

PRICES = {
    "flat tire": 25,
    "brake adjustment": 35,
    "chain replacement": 40,
}

price_tool = RepairPriceTool(PRICES)
model = OllamaModel(MODEL_NAME)

assistant = RepairAssistant(
    "Jamie",
    INSTRUCTIONS,
    price_tool,
    model,
)

print("Welcome to Bayside Bike Repair!")
print("Type a message, or type quit to stop.")

user_message = input("You: ")

while user_message != "quit":
    print(f"{assistant.name}: {assistant.respond(user_message)}")
    user_message = input("You: ")

print(f"Messages in this conversation: {len(assistant.history)}")
