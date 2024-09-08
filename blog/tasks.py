import africastalking
from django.conf import settings

africastalking.initialize(settings.AFRICASTALKING_USERNAME, settings.AFRICASTALKING_API_KEY)
sms = africastalking.SMS

def send_order_alert(customer, order):
    message = f"Dear {customer.name}, your order for {order.item} has been placed successfully."
    phone_number = f"{customer.phone_number}"
    
    try:
        response = sms.send(message, [phone_number])
        
        # Example: Log the response or check the status
        if response['SMSMessageData']['Recipients']:
            print(f"SMS sent successfully: {response}")
        else:
            print("SMS failed to send")
            
        return response
    except Exception as e:
        # Handle exceptions (e.g., network issues, invalid phone numbers)
        print(f"Failed to send SMS: {e}")
        return None
