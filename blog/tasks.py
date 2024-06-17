import africastalking
from django.conf import settings

africastalking.initialize(settings.AFRICASTALKING_USERNAME, settings.AFRICASTALKING_API_KEY)
sms = africastalking.SMS

def send_order_alert(customer, order):

    message = f"Dear {customer.name}, your order for {order.item} has been placed successfully."
    phone_number = '+254745101544'  # Replace with actual phone number field
    response = sms.send(message, [phone_number])
    