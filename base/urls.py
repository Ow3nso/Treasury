# ----- 3rd Party Libraries -----
from django.urls import path

# ----- In-Built Libraries -----
from .views import Process_Receipt

urlpatterns = [
    path("", Process_Receipt.as_view(), name="process_receipt")
]