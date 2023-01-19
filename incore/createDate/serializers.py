from createDate.models import CreateDate
from rest_framework import serializers


class CreateDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreateDate
        fields = 'date'
        
    def validate(self,value):
        if value['date'] == (r'^\d{4}$'):
            raise serializers.ValidationError('Дата не может быть пустой')
        return value