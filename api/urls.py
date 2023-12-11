# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TreasuryViews
from api import views, messenger

router = DefaultRouter()
router.register(r'Treasury', TreasuryViews, basename='Treasury')

urlpatterns = [
    path('api/', include(router.urls)),
    path('receipts/', views.ReceiptViews.as_view(), name='receipts'),
    path('receipts/<int:pk>', views.ReceiptDetail.as_view(), name='receipts'),
    path('api/numbers/', messenger.MessageViews.as_view())
    # Add more patterns as needed
]