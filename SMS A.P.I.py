
print("Hi, welcome to Chama Sacco, please provide the following details in order to register.")

name = input("Please enter your full names: ")
ID_number = input("Please Provide your ID Number: ")

print("Hi " + name + ", you have successfully registered at Chama Sacco.")

import africastalking;

username = "sandbox"
api_key = "09f50cbc3c8d51f579abae7f9430be7eb88363ee13db877203411881a9aa02b9M"

africastalking.initialize(username, api_key)

def send_sms(phone_number, message):
    sms = africastalking.SMS
    response = sms.send(message, [phone_number])

print(response)

if __name__ == "__main__":
    phone_number == "+254743075025"
    message == "Welcome to Chama Sacco!"

    send_sms(phone_number, message)