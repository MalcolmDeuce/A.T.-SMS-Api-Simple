
import africastalking

africastalking.initialize(username='userforsms', api_key='659c939f8108261fe39f36ab3248c04ad06eee0a8e2171d1cd875540e2295a79')


sms = africastalking.SMS


message = "Hello from Africa's Talking!"
recipients = ['+254743075025', '+254105202983']

try:
    response = sms.send(message, recipients)
    print(response)
    
except Exception as e:
    print("An error occurred:", e)
