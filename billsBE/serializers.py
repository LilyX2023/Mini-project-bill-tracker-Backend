from .models import Bills
from rest_framework import serializers

class BillsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Bills
        fields='__all__'