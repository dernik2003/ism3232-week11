# Bike Repair Shop Assistant
Nikita Lemeshenko

## Project Description

I made a chatbot for a bike repair shop called Bayside Bike Repair. It can check repair prices and answer basic questions about the shop. The repair prices and customer examples are made up for class. Booking and payment requests do not make changes automatically.

## Week 11 - AI Model Integration

In Week 11 I used Ollama with Granite 4.1 and a mock model for tests. The shop is open from 9 am to 6 pm Monday through Saturday. I kept repair prices in a separate Python tool instead of relying on the model to remember them.

## Week 12 - Tools and Guardrails

I updated my bike repair chatbot so the model can request the repair-price tool rather than relying on price keywords. During the real Ollama test, Jamie answered a flat tire price question correctly with $25 and greeted me when I said hello. The toolbox refused a FakeModel booking request that supplied the name Dana Cruz before the customer had typed it. In another real test, Jamie collected the customer's name, sent the flat tire booking to the approval queue, and the staff review approved it once, resulting in one confirmed booking. I added an instruction telling Jamie to greet customers who only say hello, ask for the repair type and full name before booking, and not claim a booking is confirmed before staff approves it. I also tested the order-address guardrail in Exercise 3: without it, Ollama supplied a made-up address, so I rejected the request and retained the guardrail.

The local automated test run showed 40 passing tests. The outfitters example also has a fallback model that uses keyword responses when Ollama cannot answer.

## Running the Project

Install dependencies from `requirements.txt`, and for the real model start Ollama with `granite4.1:3b`.

- Outfitters example: `python3 main.py`
- Bike repair mini-project: `python3 my_main.py`
- Tests: `pytest -v`
- Formatting and checks: `ruff format . && ruff check . && pytest -v`

## AI assistance and class explanations

The Outfitters classes follow the examples and answer keys from the instructor's Week 12 lab. AI was used to help adapt the existing Bayside Bike Repair mini-project classes. The generated code and line-by-line explanations are included in `AI_ASSISTANCE.md` for review. I should check I understand every line before submitting.
