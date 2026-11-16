# Bike Repair Shop Assistant
Nikita Lemeshenko

## Project Description

I made a chatbot for a bike repair shop called Bayside Bike Repair. It can check repair prices and answer basic questions about the shop. The repair prices and customer examples are made up for class. Booking and payment requests do not make changes automatically.

## Week 11 - AI Model Integration

In Week 11 I used Ollama with Granite 4.1 and a mock model for tests. The shop is open from 9 am to 6 pm Monday through Saturday. I kept repair prices in a separate Python tool instead of relying on the model to remember them.

## Week 12 - Tools and Guardrails

I changed my assistant so the model can ask to check a repair price instead of using keyword rules for prices. In my FakeModel test, a flat tire question used the price tool and returned $25. The toolbox also refused a booking request when the model supplied the name Dana Cruz but the customer had not typed that name. A booking goes into a waiting queue, and only staff approval adds it to the confirmed list. I added instructions telling the model to greet customers who only say hello and to collect the service and full name before requesting a booking. The fake-model tests pass without Ollama, but the real-model interaction and Exercise 3 still need to be verified on a computer running Ollama.

## Running the Project

Install dependencies from `requirements.txt`, and for the real model start Ollama with `granite4.1:3b`.

- Outfitters example: `python3 main.py`
- Bike repair mini-project: `python3 my_main.py`
- Tests: `pytest -v`
- Formatting and checks: `ruff format . && ruff check . && pytest -v`

## AI assistance and class explanations

The Outfitters classes follow the examples and answer keys from the instructor's Week 12 lab. AI was used to help adapt the existing Bayside Bike Repair mini-project classes. The generated code and line-by-line explanations are included in `AI_ASSISTANCE.md` for review. I should check I understand every line before submitting.
