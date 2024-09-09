import africastalking
from django.conf import settings

africastalking.initialize(settings.AFRICASTALKING_USERNAME, settings.AFRICASTALKING_API_KEY)
sms = africastalking.SMS

def send_order_alert(customer, order):
    message = f"Dear {customer.name}, your order for {order.item} has been placed successfully."
    phone_number = f"{customer.phone_number}"
    
    try:
        response = sms.send(message, [phone_number])
        print(f"Response: {response}")  # Log response to inspect
        # Check for specific success or error conditions in response
        if response['SMSMessageData']['Recipients']:
            print(f"SMS sent successfully: {response}")
        else:
            print("SMS sending failed. Check response details.")
    except Exception as e:
        print(f"Failed to send SMS: {e}")