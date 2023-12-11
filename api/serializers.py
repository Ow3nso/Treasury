# ----- 3rd Party Libraries -----
from rest_framework import serializers

# -----In-Built Libraries -----
from .models import Treasury

# ----- Serializer Classes -----
class TreasurySerializer(serializers.ModelSerializer):
    class Meta:
        model = Treasury
        fields = "__all__" 

class MessengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Treasury
        fields = ['phonenumber', 'receipt_url']