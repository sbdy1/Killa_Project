from rest_framework import serializers
from .models import mma

class mmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = mma
        fields = '__all__'
