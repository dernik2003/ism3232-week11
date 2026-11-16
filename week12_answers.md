# Week 12 Answers
Nikita Lemeshenko

## Exercise 1

1. The customer typed three messages: "I want to change my shipping address", "It's order A102", and "9 Pine Street, Tampa".
2. Two tool requests were refused. The first one tried A100, which the customer never gave. The second one used an address that the customer did not provide.
3. Ollama receives 14 messages: one system message, seven user/assistant messages including the new "thanks", and six messages for the three tool calls.
4. The payment rule also catches the word "card" inside "gift cards". This is okay because sending a harmless question to a person is safer than accidentally letting payment information reach the model.

## Exercise 2

I added check_return in order_tool.py, added it to toolbox.py, and added one tool test and one FakeModel chatbot test. Only delivered orders can be returned within 30 days.

## Exercise 3

With the customer-said guardrail disabled, an AI model may invent an order number and an address, and the change could be added to the staff queue even though the customer did not provide those details. A staff member could approve that incorrect address by mistake. The customer-said check is important because it refuses details before they reach the approval queue.

The reading's example of a real run: A100 and 123 Main St were made up and put into a waiting request. This is the instructor's example, **not** a claim that I reproduced it with Ollama.

**Local test still to do:** Temporarily put `return True` at the start of `Toolbox.customer_said`, run `python3 main.py` with Ollama on, ask to change an address without supplying the details, copy the actual result here, reject it at staff review, and remove `return True` again.

## Exercise 4

I added FallbackModel. It asks the first model, and if the first returns None it asks the second. The test uses SilentModel and KeywordModel, so basic order lookups still work when Ollama is unavailable.
