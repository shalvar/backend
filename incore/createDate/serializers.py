from CreateDate.models import CreateDate
from rest_framework import serializers


class CreateDateSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = CreateDate
        fields = 'date'
        

    