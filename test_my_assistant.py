# tests/test_my_assistant.py
# Author: Nikita Lemeshenko

from mock_model import MockModel
from my_assistant import RepairAssistant
from my_tool import RepairPriceTool


class NoAnswerModel:
    def reply(self, instructions, history):
        return None


def make_assistant(model):
    prices = {
        "flat tire": 25,
        "brake adjustment": 35,
        "chain replacement": 40,
    }

    tool = RepairPriceTool(prices)

    return RepairAssistant(
        "Jamie",
        "Be friendly.",
        tool,
        model,
    )


def test_tool_finds_service():
    tool = RepairPriceTool({"flat tire": 25})
    assert tool.find_service("How much for a flat tire?") == "flat tire"


def test_known_repair_price():
    assistant = make_assistant(MockModel())
    reply = assistant.respond("How much does a flat tire cost?")
    assert "$25" in reply


def test_unknown_repair():
    assistant = make_assistant(MockModel())
    reply = assistant.respond("How much does a tune-up cost?")
    assert "Which service" in reply


def test_booking_request_goes_to_employee():
    assistant = make_assistant(MockModel())
    reply = assistant.respond("I want to book a repair")
    assert "employee" in reply


def test_mock_model_answers():
    assistant = make_assistant(MockModel())
    reply = assistant.respond("hello")
    assert reply == "Hello! How can I help you today?"


def test_model_unavailable():
    assistant = make_assistant(NoAnswerModel())
    reply = assistant.respond("hello")
    assert "can't answer" in reply


def test_price_tool_works_without_model():
    assistant = make_assistant(NoAnswerModel())
    reply = assistant.respond("What is the price for brake adjustment?")
    assert "$35" in reply


def test_history_records_messages():
    assistant = make_assistant(MockModel())

    assistant.respond("hello")
    assistant.respond("How much for a flat tire?")

    assert len(assistant.history) == 4
    assert assistant.history[0]["role"] == "user"
    assert assistant.history[1]["role"] == "assistant"
