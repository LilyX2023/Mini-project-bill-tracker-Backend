from django.shortcuts import render
from .models import Bills
from rest_framework import viewsets, permissions
from .serializers import BillsSerializer

class BillsViewSet(viewsets.ModelViewSet):
    queryset = Bills.objects.all().order_by('-id')
    serializer_class=BillsSerializer
    permission_classes=[permissions.AllowAny]

# Create your views here.
