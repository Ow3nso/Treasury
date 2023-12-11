'''
# ----- 3rd Party Libraries -----
import imgkit
from collections.abc import Iterable
#from wkhtmltopdf import WKHtmlToPdf

# ----- In-Built Libraries -----
from django.db import models

# Create your models here.
class Treasure(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=10000)
    giving = models.CharField(max_length=1000)
    amount = models.FloatField()
    phonenumber = models.CharField(max_length=20)
    receipt = models.ImageField()

    def save(self, *args, **kwargs):
        self.receipt.save(imgkit.from_url('http://google.com', False), save=False)
        
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
'''
    

import imgkit
import pdfkit
import subprocess
from django.db import models
from django.core.files.base import ContentFile
from django.template.loader import render_to_string

# ----- check if instance exists -----
class Check:
    @staticmethod
    def checkInstance(self):
        # Check if the instance exists
        try:
            self.refresh_from_db()
        except Treasury.DoesNotExist:
            # Log an error or handle the case where the instance does not exist
            print(f"Error: Treasury instance with ID {self.id} does not exist.")
            return

# ----- convert HTML to pdf -----
class Conversion:
    @staticmethod
    def convertHtmlToPdf(self):
        # Save HTML content to a file
        html_content = self.render_html()
        html_file_path = f"/home/ow3nso/projects/python/django/excel3/{self.id}_receipt.html"  # Replace with your desired path
        with open(html_file_path, 'w') as html_file:
            html_file.write(html_content)

        # Convert the HTML to PDF
        pdf_file_path = f"/home/ow3nso/projects/python/django/excel3/{self.id}_receipt.pdf"  # Replace with your desired path
        try:
            # Use subprocess to call wkhtmltopdf
            subprocess.run(['wkhtmltopdf', html_file_path, pdf_file_path], check=True)

            # Read the generated PDF file
            with open(pdf_file_path, 'rb') as pdf_file:
                # Save the PDF file to the model's FileField
                self.receipt_pdf.save(f'receipt_{self.id}.pdf', ContentFile(pdf_file.read()), save=True)

        except subprocess.CalledProcessError as e:
            # Handle the subprocess error (e.g., log it, display an error message)
            print(f"Error converting to PDF: {e}")

# ----- Render HTMl page -----
class Render:
    @staticmethod
    def render_html(self):
        # Customize this method to render the HTML content based on your model instance data
        context = {'instance': self}
        html_content = render_to_string('receipt.html', context)
        return html_content



class Treasury(models.Model):
    name = models.CharField(max_length=10000)
    giving = models.CharField(max_length=1000)
    amount = models.FloatField()
    phonenumber = models.CharField(max_length=20)
    receipt_number = models.BigIntegerField(unique=True)
    receipt_url = models.CharField(max_length=1000, blank=True, null=True)
    
    def save(self, *args, **kwargs):

        #check if receipt number exists
        if Treasury.objects.filter(receipt_number=self.receipt_number):
            pass
        else:
            # Save the image
            super().save(*args, **kwargs)

            # Convert the HTML to PDF
            receipt_id = str(self.id)
            url = "http://127.0.0.1:8000/api/receipts/" + receipt_id

            self.receipt_url = url
            
            super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    
