# ----- 3rd Party Libraries -----
import pandas as pd
from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.parsers import MultiPartParser, FormParser

# ----- In-Bult Libraries -----
from .models import Treasury
from .serializers import TreasurySerializer


# ----- Create your views here. -----
class TreasuryViews(viewsets.ModelViewSet):
    queryset = Treasury.objects.all()
    serializer_class = TreasurySerializer

    parser_classes = [MultiPartParser, FormParser]

    def create(self, request, *args, **kwargs):
        
        file = request.data.get('file')

        if file:
            # Read Excel file using pandas
            excel_data = pd.read_excel(file, engine='openpyxl')

            grouped_data = excel_data.groupby('name')

            # Loop through rows and save to the database
            for name, row in excel_data.iterrows():
                Treasury.objects.create(
                    name=name,
                    giving=row['Giving'],
                    amount=row['Amount']
                )

            return Response({'status': 'success', 'message': 'Data imported successfully'})

        return Response({'status': 'error', 'message': 'No file provided'})

    
class ReceiptViews(generics.ListAPIView):
    queryset = Treasury.objects.all()
    serializer_class = TreasurySerializer

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'all_receipts.html'

    def get(self, request):
        queryset = Treasury.objects.all()
        return Response({'receipts':queryset})
    
class ReceiptDetail(generics.RetrieveAPIView):
    queryset = Treasury.objects.all()
    serializer_class = TreasurySerializer

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'receipt.html'

    def get(self, request, pk:int):
        queryset = Treasury.objects.get(pk=pk)
        return Response({'receipts':queryset})