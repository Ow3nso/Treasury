# ----- 3rd Party Libraries -----
import pandas as pd
from tablib import Dataset
from django.views import View
from django.shortcuts import render
from rest_framework.parsers import MultiPartParser

# ----- In-Built Libraries -----
from .models import Process_Statement
from .resources import Process_Statement_Resource

# Create your views here.
class Process_Receipt(View):
    #parser_classes = [parsers.MultiPartParser]
    template_name = "form_template.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    

    def post(self, request, *args, **kwargs):
    
        file = request.FILES['excel']

        if file:
            # Read Excel file using pandas
            excel_data = pd.read_excel(file, engine='openpyxl')

            #grouped_data = excel_data.groupby('name')

            # Loop through rows and save to the database
            for name, row in excel_data.iterrows():
                Process_Statement.objects.create(
                    name=row['name'],
                    giving=row['giving'],
                    amount=row['amount']
                )

        context={}
        return render(request, self.template_name, context)