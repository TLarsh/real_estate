from rest_framework import serializers
from .models import Realtor


class RealtorSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Realtor
        fields = '__all__'