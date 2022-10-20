from rest_framework import serializers
from .models import DataTS

class DataTSSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataTS
        fields = '__all__'