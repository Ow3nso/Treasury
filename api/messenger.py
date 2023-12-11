# ----- 3rd Party Libraries -----
import imgkit
import pywhatkit as kit
import subprocess
import time
import datetime
import json
import requests
from django.core.files.base import ContentFile
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

# ----- In-Built Libraries -----
from api.models import Treasury
from .serializers import *

class Copyq:
    def start_copyq_server():
        try:
            # Start CopyQ server
            subprocess.run(['copyq', 'start'])
            
            # Wait for some time to ensure the server has started
            time.sleep(2)
            
            print("CopyQ server started successfully!")

        except Exception as e:
            print(f"Error starting CopyQ server: {e}")
    
class MessageViews(generics.ListCreateAPIView):
    queryset = Treasury.objects.all()
    serializer_class = MessengerSerializer

     
    def send_messages(self):
        queryset = Treasury.objects.all()
        for treasure_obj in queryset:
            # Assuming your Treasure model has a 'phone_number' field
            sign = "+"
            phone_number = sign+treasure_obj.phonenumber
            receipt_url = treasure_obj.receipt_url
            output_path = "/home/ow3nso/projects/python/django/excel3/receipts/"+str(treasure_obj.receipt_number)+".png"

            imgkit.from_url(receipt_url, output_path)
            #print(output_path)

            
            
            try:
                kit.sendwhats_image(phone_number, output_path)
            except Exception as e:
                print(f"Error sending image: {e}")

    
    def list(self, request, *args, **kwargs):
        # Call the send_messages method when the API is accessed
        self.send_messages()
        return super().list(request, *args, **kwargs)

    
#phonenumber, message = Data.person1()

#kit.sendwhatmsg_instantly(phonenumber, message)

# Download the image from the URL and save it locally
            #img_file_path = f"{treasure_obj.id}_receipt.jpg"
            #try:
                # Instead of passing ImageFieldFile to imgkit.from_url, pass the actual file path
             #   img_file_path_str = str(treasure_obj.receipt_url)
                # Now use imgkit.from_file instead of imgkit.from_url
              #  message = imgkit.from_file(img_file_path_str, False)
                # Use subprocess to call wkhtmltopdf
               # subprocess.run(['wkhtmltopdf', receipt_url, message], check=True)

                # Read the generated PDF file
                #with open(img_file_path, 'rb') as img_file:
                    # Save the PDF file to the model's FileField
                 #   treasure_obj.receipt_url.save(f'receipt_{treasure_obj.id}.jpg', ContentFile(img_file.read()), save=True)

            #except subprocess.CalledProcessError as e:
                # Handle the subprocess error (e.g., log it, display an error message)
             #   print(f"Error converting to PDF: {e}")