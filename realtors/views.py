from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import permissions
from .models import Realtor
from .serializers import RealtorSerilizer

class RealtorListView(ListAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Realtor.objects.all()
    serializer_class = RealtorSerilizer
    pagination_class = None
    
class RealtorView(RetrieveAPIView):
    queryset = Realtor.objects.all()
    serializer_class = RealtorSerilizer
    
class TopSellerView(ListAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Realtor.objects.filter(top_seller=True)
    serializer_class = RealtorSerilizer
    pagination_class = None
    
