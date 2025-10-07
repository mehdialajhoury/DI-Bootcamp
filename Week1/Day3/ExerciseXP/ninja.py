"""Exercise 1 : Call History

Instructions

Create a class called Phone. This class takes a parameter called phone_number. When instantiating an object create an attribute called call_history which value is an empty list.

Add a method called call that takes both self and other_phone (i.e another Phone object) as parameters. The method should print a string stating who called who, and add this string to the phone’s call_history.

Add a method called show_call_history. This method should print the call_history.

Add another attribute called messages to your __init__() method which value is an empty list.

Create a method called send_message which is similar to the call method. Each message should be saved as a dictionary with the following keys:
to : the number of another Phone object
from : your phone number (also a Phone object)
content

Create the following methods: show_outgoing_messages(self), show_incoming_messages(self), show_messages_from(self)

Test your code !!!
"""

class Phone:
    def __init__(self,phone_number):
        self.phone_number = phone_number
        self.call_history = []
        self.message = []

    def call(self,other_phone):
        string_call = (f"{other_phone.phone_number} calls {self.phone_number}")
        self.call_history.append(string_call)

    def call_history(self):
        print(self.call_history)

    def send_message(self,other_phone,message):
        dict_message = {}
        dict_message["to"] = other_phone.phone_number
        dict_message["from"] = self.phone_number
        dict_message["message"] = message
        self.message.append(dict_message)
        other_phone.message.append(dict_message)

    def show_outgoing_messages(self):
        for message in self.message:
            if message["from"] == self.phone_number:
                print(f"To {message['to']}: {message['message']}")

    def show_incoming_messages(self):
        print("Incoming Messages:")
        for message in self.message:
            if message["to"] == self.phone_number:
                print(f"From {message['from']}: {message['message']}")

    def show_messages_from(self, phone_number):
        print(f"Messages from {phone_number}:")
        for msg in self.message:
            if msg["from"] == phone_number and msg["to"] == self.phone_number:
                print(msg["message"])

    

Mehdi_phone = Phone("0771018288")

friend_Mehdi = Phone("0662729382")

Mehdi_phone.send_message(friend_Mehdi,"hello how are you ?")

Mehdi_phone.show_outgoing_messages()
friend_Mehdi.show_incoming_messages()
friend_Mehdi.show_messages_from("0771018288")