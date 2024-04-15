from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .celery_tasks import send_email_task

class SendMailView(APIView):
    def post(self,request,*args, **kwargs):
        data = request.data
        subject = data['subject']
        message = data['msg']
        recipient_list = data['recipient_list']
        send_email_task.delay(subject, message, recipient_list)
        return Response({'message': 'Email sent asynchronously'}, status=status.HTTP_200_OK)
