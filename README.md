# Bike Repair Shop Assistant
Nikita Lemeshenko

## Project Description

For my mini-project, I created a chatbot for a bike repair shop called Bayside Bike Repair. The assistant helps customers check repair prices and get basic information about the shop. I used a separate Python class to store repair prices instead of putting that information directly into the chatbot. The repair information is made up for this project, and no real customer information is used. Booking and payment requests are passed to an employee because the chatbot should not make changes without someone checking them first.

## Week 11 - AI Model Integration

I updated my assistant to use Ollama with the Granite 4.1 model. When I asked about the shop's opening hours, the model used the information in its instructions to answer that the shop is open from 9 am to 6 pm, Monday through Saturday. When I asked about free pickup, it could not confirm that service because it was not included in the instructions. I decided to keep repair prices and appointment requests controlled by Python code because giving incorrect prices or making unauthorized bookings could cause problems for customers. I also added tests using a mock model to make sure the assistant still handles important requests when Ollama is unavailable.

## Running the Project

Install the packages listed in requirements.txt and make sure Ollama is running with the granite4.1:3b model.

Run the assistant:

`python3 my_main.py`

Run the tests:

`pytest -v`