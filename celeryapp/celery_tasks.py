from PIL import Image
import os
from celery import shared_task
from django.core.mail import send_mail
from .models import Order

@shared_task
def send_email_task(subject, message, recipient_list):
    send_mail(subject, message, 'from@example.com', recipient_list)

@shared_task
def process_image_task(image_path):
    with Image.open(image_path) as img:
        # Perform image processing operations here
        # For example, resize the image
        resized_img = img.resize((200, 200))
        # Save the processed image
        processed_image_path = image_path.replace('.jpg', '_resized.jpg')
        resized_img.save(processed_image_path)

    # Clean up the original image file
    os.remove(image_path)
    return processed_image_path

@shared_task
def working_with_orders_data(order_data):
    order_data = Order.objects.all()

    order_details = {'orders':[name for name in order_data.name]}