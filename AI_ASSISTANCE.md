# AI Assistance: Generated Class Code and Line-by-Line Explanation

The new and adapted bike shop classes were drafted with AI assistance. The exact generated source is pasted below, followed by numbered comments explaining what each nonblank line does and why. Read and check the code before submitting.

## my_tool.py

```python
# my_tool.py
# Author: Nikita Lemeshenko


class RepairPriceTool:
    """Keep the shop's repair prices and record approved bookings."""

    def __init__(self, prices):
        """Save repair prices and start with no confirmed bookings."""
        self.prices = prices
        self.bookings = []

    def find_service(self, text):
        """Find a known repair service in the text."""
        for service in self.prices:
            if service in text.lower():
                return service
        return None

    def price_for(self, service):
        """Return a price, or None when the service is not known."""
        return self.prices.get(service)

    def check_repair_price(self, service):
        """Look up the price of one bike repair.

        Args:
            service: The repair name, like flat tire.
        """
        found = self.find_service(service)
        if found is None:
            return "I can check flat tire, brake adjustment, or chain replacement."
        return f"The price for {found} is ${self.price_for(found)}."

    def add_booking(self, service, customer_name):
        """Record a booking after a person has approved it."""
        self.bookings.append({"service": service, "customer_name": customer_name})
```

### Line comments

- Line 1 (`# my_tool.py`): Labels the file, author, or project setting for easier review.
- Line 2 (`# Author: Nikita Lemeshenko`): Labels the file, author, or project setting for easier review.
- Line 5 (`class RepairPriceTool:`): Creates a class to keep this part of the program separate and reusable.
- Line 6 (`"""Keep the shop's repair prices and record approved bookings."""`): Documents what this code is for and what values its user should provide.
- Line 8 (`def __init__(self, prices):`): Defines this method so the object has one specific responsibility.
- Line 9 (`"""Save repair prices and start with no confirmed bookings."""`): Documents what this code is for and what values its user should provide.
- Line 10 (`self.prices = prices`): Saves state on this object for use by other methods.
- Line 11 (`self.bookings = []`): Saves state on this object for use by other methods.
- Line 13 (`def find_service(self, text):`): Defines this method so the object has one specific responsibility.
- Line 14 (`"""Find a known repair service in the text."""`): Documents what this code is for and what values its user should provide.
- Line 15 (`for service in self.prices:`): Iterates through the available items rather than guessing.
- Line 16 (`if service in text.lower():`): Checks a condition so unsafe or invalid requests follow a safer path.
- Line 17 (`return service`): Returns a result immediately so the next step can use it.
- Line 18 (`return None`): Returns a result immediately so the next step can use it.
- Line 20 (`def price_for(self, service):`): Defines this method so the object has one specific responsibility.
- Line 21 (`"""Return a price, or None when the service is not known."""`): Documents what this code is for and what values its user should provide.
- Line 22 (`return self.prices.get(service)`): Returns a result immediately so the next step can use it.
- Line 24 (`def check_repair_price(self, service):`): Defines this method so the object has one specific responsibility.
- Line 25 (`"""Look up the price of one bike repair.`): Documents what this code is for and what values its user should provide.
- Line 27 (`Args:`): Documents what this code is for and what values its user should provide.
- Line 28 (`service: The repair name, like flat tire.`): Completes the method's current step as part of the model, validation, or approval flow.
- Line 29 (`"""`): Documents what this code is for and what values its user should provide.
- Line 30 (`found = self.find_service(service)`): Completes the method's current step as part of the model, validation, or approval flow.
- Line 31 (`if found is None:`): Checks a condition so unsafe or invalid requests follow a safer path.
- Line 32 (`return "I can check flat tire, brake adjustment, or chain replacement."`): Returns a result immediately so the next step can use it.
- Line 33 (`return f"The price for {found} is ${self.price_for(found)}."`): Returns a result immediately so the next step can use it.
- Line 35 (`def add_booking(self, service, customer_name):`): Defines this method so the object has one specific responsibility.
- Line 36 (`"""Record a booking after a person has approved it."""`): Documents what this code is for and what values its user should provide.
- Line 37 (`self.bookings.append({"service": service, "customer_name": customer_name})`): Adds a message or request to the appropriate history or queue.

## repair_booking_queue.py

```python
# repair_booking_queue.py
# Author: Nikita Lemeshenko


class RepairBookingQueue:
    """Hold booking requests until an employee approves them."""

    def __init__(self, price_tool):
        """Keep the repair tool and an empty list of requests."""
        self.price_tool = price_tool
        self.requests = []

    def request_repair_booking(self, service, customer_name):
        """Request a repair booking without confirming it.

        Args:
            service: The repair name, like flat tire.
            customer_name: The customer's full name.
        """
        service = service.strip().lower()
        if service not in self.price_tool.prices:
            return "That repair service was not found."
        number = len(self.requests) + 1
        self.requests.append(
            {
                "number": number,
                "service": service,
                "customer_name": customer_name,
                "status": "waiting",
            }
        )
        return f"Request {number} was sent to staff. The repair is not booked yet."

    def waiting(self):
        """List only requests that still need a decision."""
        return [request for request in self.requests if request["status"] == "waiting"]

    def find(self, number):
        """Find a request by number."""
        for request in self.requests:
            if request["number"] == number:
                return request
        return None

    def approve(self, number):
        """Approve and book a request once."""
        request = self.find(number)
        if request is None:
            return f"There is no request {number}."
        if request["status"] != "waiting":
            return f"Request {number} is already {request['status']}."
        request["status"] = "approved"
        self.price_tool.add_booking(request["service"], request["customer_name"])
        return f"Request {number} approved."

    def reject(self, number):
        """Reject a request without creating a booking."""
        request = self.find(number)
        if request is None:
            return f"There is no request {number}."
        if request["status"] != "waiting":
            return f"Request {number} is already {request['status']}."
        request["status"] = "rejected"
        return f"Request {number} rejected."
```

### Line comments

- Line 1 (`# repair_booking_queue.py`): Labels the file, author, or project setting for easier review.
- Line 2 (`# Author: Nikita Lemeshenko`): Labels the file, author, or project setting for easier review.
- Line 5 (`class RepairBookingQueue:`): Creates a class to keep this part of the program separate and reusable.
- Line 6 (`"""Hold booking requests until an employee approves them."""`): Documents what this code is for and what values its user should provide.
- Line 8 (`def __init__(self, price_tool):`): Defines this method so the object has one specific responsibility.
- Line 9 (`"""Keep the repair tool and an empty list of requests."""`): Documents what this code is for and what values its user should provide.
- Line 10 (`self.price_tool = price_tool`): Saves state on this object for use by other methods.
- Line 11 (`self.requests = []`): Saves state on this object for use by other methods.
- Line 13 (`def request_repair_booking(self, service, customer_name):`): Defines this method so the object has one specific responsibility.
- Line 14 (`"""Request a repair booking without confirming it.`): Documents what this code is for and what values its user should provide.
- Line 16 (`Args:`): Documents what this code is for and what values its user should provide.
- Line 17 (`service: The repair name, like flat tire.`): Completes the method's current step as part of the model, validation, or approval flow.
- Line 18 (`customer_name: The customer's full name.`): Completes the method's current step as part of the model, validation, or approval flow.
- Line 19 (`"""`): Documents what this code is for and what values its user should provide.
- Line 20 (`service = service.strip().lower()`): Completes the method's current step as part of the model, validation, or approval flow.
- Line 21 (`if service not in self.price_tool.prices:`): Checks a condition so unsafe or invalid requests follow a safer path.
- Line 22 (`return "That repair service was not found."`): Returns a result immediately so the next step can use it.
- Line 23 (`number = len(self.requests) + 1`): Handles request data without directly applying a change.
- Line 24 (`self.requests.append(`): Adds a message or request to the appropriate history or queue.
- Line 25 (`{`): Completes the method's current step as part of the model, validation, or approval flow.
- Line 26 (`"number": number,`): Defines a value or explanation used by the method.
- Line 27 (`"service": service,`): Defines a value or explanation used by the method.
- Line 28 (`"customer_name": customer_name,`): Defines a value or explanation used by the method.
- Line 29 (`"status": "waiting",`): Defines a value or explanation used by the method.
- Line 30 (`}`): Closes the collection or expression opened above.
- Line 31 (`)`): Closes the collection or expression opened above.
- Line 32 (`return f"Request {number} was sent to staff. The repair is not booked yet."`): Returns a result immediately so the next step can use it.
- Line 34 (`def waiting(self):`): Defines this method so the object has one specific responsibility.
- Line 35 (`"""List only requests that still need a decision."""`): Documents what this code is for and what values its user should provide.
- Line 36 (`return [request for request in self.requests if request["status"] == "waiting"]`): Returns a result immediately so the next step can use it.
- Line 38 (`def find(self, number):`): Defines this method so the object has one specific responsibility.
- Line 39 (`"""Find a request by number."""`): Documents what this code is for and what values its user should provide.
- Line 40 (`for request in self.requests:`): Iterates through the available items rather than guessing.
- Line 41 (`if request["number"] == number:`): Checks a condition so unsafe or invalid requests follow a safer path.
- Line 42 (`return request`): Returns a result immediately so the next step can use it.
- Line 43 (`return None`): Returns a result immediately so the next step can use it.
- Line 45 (`def approve(self, number):`): Defines this method so the object has one specific responsibility.
- Line 46 (`"""Approve and book a request once."""`): Documents what this code is for and what values its user should provide.
- Line 47 (`request = self.find(number)`): Handles request data without directly applying a change.
- Line 48 (`if request is None:`): Checks a condition so unsafe or invalid requests follow a safer path.
- Line 49 (`return f"There is no request {number}."`): Returns a result immediately so the next step can use it.
- Line 50 (`if request["status"] != "waiting":`): Checks a condition so unsafe or invalid requests follow a safer path.
- Line 51 (`return f"Request {number} is already {request['status']}."`): Returns a result immediately so the next step can use it.
- Line 52 (`request["status"] = "approved"`): Handles request data without directly applying a change.
- Line 53 (`self.price_tool.add_booking(request["service"], request["customer_name"])`): Handles request data without directly applying a change.
- Line 54 (`return f"Request {number} approved."`): Returns a result immediately so the next step can use it.
- Line 56 (`def reject(self, number):`): Defines this method so the object has one specific responsibility.
- Line 57 (`"""Reject a request without creating a booking."""`): Documents what this code is for and what values its user should provide.
- Line 58 (`request = self.find(number)`): Handles request data without directly applying a change.
- Line 59 (`if request is None:`): Checks a condition so unsafe or invalid requests follow a safer path.
- Line 60 (`return f"There is no request {number}."`): Returns a result immediately so the next step can use it.
- Line 61 (`if request["status"] != "waiting":`): Checks a condition so unsafe or invalid requests follow a safer path.
- Line 62 (`return f"Request {number} is already {request['status']}."`): Returns a result immediately so the next step can use it.
- Line 63 (`request["status"] = "rejected"`): Handles request data without directly applying a change.
- Line 64 (`return f"Request {number} rejected."`): Returns a result immediately so the next step can use it.

## repair_toolbox.py

```python
# repair_toolbox.py
# Author: Nikita Lemeshenko


class RepairToolbox:
    """Check every tool request before the model can use it."""

    def __init__(self, price_tool, booking_queue):
        """Store the price lookup and approval queue."""
        self.price_tool = price_tool
        self.booking_queue = booking_queue

    def tool_list(self):
        """List the two methods that the model may request."""
        return [
            self.price_tool.check_repair_price,
            self.booking_queue.request_repair_booking,
        ]

    def clean(self, arguments, key):
        """Get one requested value as trimmed text."""
        return str(arguments.get(key, "")).strip()

    def customer_said(self, history, text):
        """Check only messages originally typed by the customer."""
        for message in history:
            if message["role"] == "user" and text.lower() in message["content"].lower():
                return True
        return False

    def run(self, name, arguments, history):
        """Refuse unknown tools, empty details, and invented booking details."""
        if name == "check_repair_price":
            service = self.clean(arguments, "service")
            if service == "":
                return "Please ask which repair the customer wants."
            return self.price_tool.check_repair_price(service)
        if name == "request_repair_booking":
            service = self.clean(arguments, "service")
            customer_name = self.clean(arguments, "customer_name")
            if service == "" or customer_name == "":
                return "Ask for both the repair service and customer's full name."
            if not self.customer_said(history, service):
                return "The customer has not given that repair service. Ask them."
            if not self.customer_said(history, customer_name):
                return "The customer has not given that name. Ask them."
            return self.booking_queue.request_repair_booking(service, customer_name)
        return f"There is no tool named {name}."
```

### Line comments

- Line 1 (`# repair_toolbox.py`): Labels the file, author, or project setting for easier review.
- Line 2 (`# Author: Nikita Lemeshenko`): Labels the file, author, or project setting for easier review.
- Line 5 (`class RepairToolbox:`): Creates a class to keep this part of the program separate and reusable.
- Line 6 (`"""Check every tool request before the model can use it."""`): Documents what this code is for and what values its user should provide.
- Line 8 (`def __init__(self, price_tool, booking_queue):`): Defines this method so the object has one specific responsibility.
- Line 9 (`"""Store the price lookup and approval queue."""`): Documents what this code is for and what values its user should provide.
- Line 10 (`self.price_tool = price_tool`): Saves state on this object for use by other methods.
- Line 11 (`self.booking_queue = booking_queue`): Saves state on this object for use by other methods.
- Line 13 (`def tool_list(self):`): Defines this method so the object has one specific responsibility.
- Line 14 (`"""List the two methods that the model may request."""`): Documents what this code is for and what values its user should provide.
- Line 15 (`return [`): Returns a result immediately so the next step can use it.
- Line 16 (`self.price_tool.check_repair_price,`): Completes the method's current step as part of the model, validation, or approval flow.
- Line 17 (`self.booking_queue.request_repair_booking,`): Handles request data without directly applying a change.
- Line 18 (`]`): Closes the collection or expression opened above.
- Line 20 (`def clean(self, arguments, key):`): Defines this method so the object has one specific responsibility.
- Line 21 (`"""Get one requested value as trimmed text."""`): Documents what this code is for and what values its user should provide.
- Line 22 (`return str(arguments.get(key, "")).strip()`): Returns a result immediately so the next step can use it.
- Line 24 (`def customer_said(self, history, text):`): Defines this method so the object has one specific responsibility.
- Line 25 (`"""Check only messages originally typed by the customer."""`): Documents what this code is for and what values its user should provide.
- Line 26 (`for message in history:`): Iterates through the available items rather than guessing.
- Line 27 (`if message["role"] == "user" and text.lower() in message["content"].lower():`): Checks a condition so unsafe or invalid requests follow a safer path.
- Line 28 (`return True`): Returns a result immediately so the next step can use it.
- Line 29 (`return False`): Returns a result immediately so the next step can use it.
- Line 31 (`def run(self, name, arguments, history):`): Defines this method so the object has one specific responsibility.
- Line 32 (`"""Refuse unknown tools, empty details, and invented booking details."""`): Documents what this code is for and what values its user should provide.
- Line 33 (`if name == "check_repair_price":`): Checks a condition so unsafe or invalid requests follow a safer path.
- Line 34 (`service = self.clean(arguments, "service")`): Reads tool arguments that must be checked instead of trusted automatically.
- Line 35 (`if service == "":`): Checks a condition so unsafe or invalid requests follow a safer path.
- Line 36 (`return "Please ask which repair the customer wants."`): Returns a result immediately so the next step can use it.
- Line 37 (`return self.price_tool.check_repair_price(service)`): Returns a result immediately so the next step can use it.
- Line 38 (`if name == "request_repair_booking":`): Checks a condition so unsafe or invalid requests follow a safer path.
- Line 39 (`service = self.clean(arguments, "service")`): Reads tool arguments that must be checked instead of trusted automatically.
- Line 40 (`customer_name = self.clean(arguments, "customer_name")`): Reads tool arguments that must be checked instead of trusted automatically.
- Line 41 (`if service == "" or customer_name == "":`): Checks a condition so unsafe or invalid requests follow a safer path.
- Line 42 (`return "Ask for both the repair service and customer's full name."`): Returns a result immediately so the next step can use it.
- Line 43 (`if not self.customer_said(history, service):`): Checks a condition so unsafe or invalid requests follow a safer path.
- Line 44 (`return "The customer has not given that repair service. Ask them."`): Returns a result immediately so the next step can use it.
- Line 45 (`if not self.customer_said(history, customer_name):`): Checks a condition so unsafe or invalid requests follow a safer path.
- Line 46 (`return "The customer has not given that name. Ask them."`): Returns a result immediately so the next step can use it.
- Line 47 (`return self.booking_queue.request_repair_booking(service, customer_name)`): Returns a result immediately so the next step can use it.
- Line 48 (`return f"There is no tool named {name}."`): Returns a result immediately so the next step can use it.

## my_assistant.py

```python
# my_assistant.py
# Author: Nikita Lemeshenko

HANDOFF_WORDS = ["cancel", "reschedule", "payment", "card"]
MAX_TOOL_ROUNDS = 3


class RepairAssistant:
    """Let a model choose tools but check requests and protect sensitive actions."""

    def __init__(self, name, instructions, tools, model):
        """Set the assistant's name, instructions, toolbox, model, and history."""
        self.name = name
        self.instructions = instructions
        self.tools = tools
        self.model = model
        self.history = []

    def respond(self, user_message):
        """Save the question and the answer to the conversation history."""
        self.history.append({"role": "user", "content": user_message})
        reply = self.choose_reply(user_message)
        self.history.append({"role": "assistant", "content": reply})
        return reply

    def choose_reply(self, user_message):
        """Send risky questions to staff before asking the model."""
        if self.needs_human(user_message.lower()):
            return "I can't change or cancel that here. Please speak to an employee."
        return self.model_reply()

    def needs_human(self, text):
        """Check for actions that must be handled directly by an employee."""
        for word in HANDOFF_WORDS:
            if word in text:
                return True
        return False

    def model_reply(self):
        """Run at most three checked tool calls before returning a reply."""
        rounds = 0
        while rounds < MAX_TOOL_ROUNDS:
            decision = self.model.decide(
                self.instructions, self.history, self.tools.tool_list()
            )
            if decision is None:
                return "Sorry, I can't answer that right now. Please ask an employee."
            if "text" in decision:
                return decision["text"]
            name = decision["tool"]
            arguments = decision["arguments"]
            result = self.tools.run(name, arguments, self.history)
            self.history.append(
                {
                    "role": "tool",
                    "tool_name": name,
                    "arguments": arguments,
                    "content": result,
                }
            )
            rounds += 1
        return "Sorry, I couldn't finish that. Please speak to an employee."
```

### Line comments

- Line 1 (`# my_assistant.py`): Labels the file, author, or project setting for easier review.
- Line 2 (`# Author: Nikita Lemeshenko`): Labels the file, author, or project setting for easier review.
- Line 4 (`HANDOFF_WORDS = ["cancel", "reschedule", "payment", "card"]`): Keeps a safety setting visible in one place.
- Line 5 (`MAX_TOOL_ROUNDS = 3`): Keeps a safety setting visible in one place.
- Line 8 (`class RepairAssistant:`): Creates a class to keep this part of the program separate and reusable.
- Line 9 (`"""Let a model choose tools but check requests and protect sensitive actions."""`): Documents what this code is for and what values its user should provide.
- Line 11 (`def __init__(self, name, instructions, tools, model):`): Defines this method so the object has one specific responsibility.
- Line 12 (`"""Set the assistant's name, instructions, toolbox, model, and history."""`): Documents what this code is for and what values its user should provide.
- Line 13 (`self.name = name`): Saves state on this object for use by other methods.
- Line 14 (`self.instructions = instructions`): Saves state on this object for use by other methods.
- Line 15 (`self.tools = tools`): Saves state on this object for use by other methods.
- Line 16 (`self.model = model`): Saves state on this object for use by other methods.
- Line 17 (`self.history = []`): Saves state on this object for use by other methods.
- Line 19 (`def respond(self, user_message):`): Defines this method so the object has one specific responsibility.
- Line 20 (`"""Save the question and the answer to the conversation history."""`): Documents what this code is for and what values its user should provide.
- Line 21 (`self.history.append({"role": "user", "content": user_message})`): Adds a message or request to the appropriate history or queue.
- Line 22 (`reply = self.choose_reply(user_message)`): Completes the method's current step as part of the model, validation, or approval flow.
- Line 23 (`self.history.append({"role": "assistant", "content": reply})`): Adds a message or request to the appropriate history or queue.
- Line 24 (`return reply`): Returns a result immediately so the next step can use it.
- Line 26 (`def choose_reply(self, user_message):`): Defines this method so the object has one specific responsibility.
- Line 27 (`"""Send risky questions to staff before asking the model."""`): Documents what this code is for and what values its user should provide.
- Line 28 (`if self.needs_human(user_message.lower()):`): Checks a condition so unsafe or invalid requests follow a safer path.
- Line 29 (`return "I can't change or cancel that here. Please speak to an employee."`): Returns a result immediately so the next step can use it.
- Line 30 (`return self.model_reply()`): Returns a result immediately so the next step can use it.
- Line 32 (`def needs_human(self, text):`): Defines this method so the object has one specific responsibility.
- Line 33 (`"""Check for actions that must be handled directly by an employee."""`): Documents what this code is for and what values its user should provide.
- Line 34 (`for word in HANDOFF_WORDS:`): Iterates through the available items rather than guessing.
- Line 35 (`if word in text:`): Checks a condition so unsafe or invalid requests follow a safer path.
- Line 36 (`return True`): Returns a result immediately so the next step can use it.
- Line 37 (`return False`): Returns a result immediately so the next step can use it.
- Line 39 (`def model_reply(self):`): Defines this method so the object has one specific responsibility.
- Line 40 (`"""Run at most three checked tool calls before returning a reply."""`): Documents what this code is for and what values its user should provide.
- Line 41 (`rounds = 0`): Completes the method's current step as part of the model, validation, or approval flow.
- Line 42 (`while rounds < MAX_TOOL_ROUNDS:`): Repeats model decisions only while below the safety limit.
- Line 43 (`decision = self.model.decide(`): Completes the method's current step as part of the model, validation, or approval flow.
- Line 44 (`self.instructions, self.history, self.tools.tool_list()`): Records or reads conversation history to keep decisions grounded.
- Line 45 (`)`): Closes the collection or expression opened above.
- Line 46 (`if decision is None:`): Checks a condition so unsafe or invalid requests follow a safer path.
- Line 47 (`return "Sorry, I can't answer that right now. Please ask an employee."`): Returns a result immediately so the next step can use it.
- Line 48 (`if "text" in decision:`): Checks a condition so unsafe or invalid requests follow a safer path.
- Line 49 (`return decision["text"]`): Returns a result immediately so the next step can use it.
- Line 50 (`name = decision["tool"]`): Completes the method's current step as part of the model, validation, or approval flow.
- Line 51 (`arguments = decision["arguments"]`): Reads tool arguments that must be checked instead of trusted automatically.
- Line 52 (`result = self.tools.run(name, arguments, self.history)`): Records or reads conversation history to keep decisions grounded.
- Line 53 (`self.history.append(`): Adds a message or request to the appropriate history or queue.
- Line 54 (`{`): Completes the method's current step as part of the model, validation, or approval flow.
- Line 55 (`"role": "tool",`): Defines a value or explanation used by the method.
- Line 56 (`"tool_name": name,`): Defines a value or explanation used by the method.
- Line 57 (`"arguments": arguments,`): Defines a value or explanation used by the method.
- Line 58 (`"content": result,`): Defines a value or explanation used by the method.
- Line 59 (`}`): Closes the collection or expression opened above.
- Line 60 (`)`): Closes the collection or expression opened above.
- Line 61 (`rounds += 1`): Counts tool attempts to prevent an endless loop.
- Line 62 (`return "Sorry, I couldn't finish that. Please speak to an employee."`): Returns a result immediately so the next step can use it.

