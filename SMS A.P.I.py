
import africastalking

africastalking.initialize(username='username', api_key='apikey')


sms = africastalking.SMS


message = "Hello from Africa's Talking!"
recipients = ['+254xxxxxxxxxx', '+254xxxxxxxxxx']

try:
    response = sms.send(message, recipients)
    print(response)
    
except Exception as e:
    print("An error occurred:", e)
