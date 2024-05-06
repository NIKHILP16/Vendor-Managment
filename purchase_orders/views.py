from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import *
from .models import *
from .serializers import *
from rest_framework.response import Response
from django.utils import timezone
from django.db.models import Avg
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, status


class PurchaseOrderListCreateView(generics.ListCreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class PurchaseOrderRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class AcknowledgePurchaseOrderView(generics.CreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

    def create(self, request, *args, **kwargs):
        if request.data.get('acknowledgment_date'):
            instance = self.get_object()
            instance.acknowledgment_date = request.data.get('acknowledgment_date')   
            instance.save()
            response_times = PurchaseOrder.objects.filter(vendor=instance.vendor, acknowledgment_date__isnull=False).values_list('acknowledgment_date', 'issue_date')
            total_seconds = sum(abs((ack_date - issue_date).total_seconds()) for ack_date, issue_date in response_times) 
            try:
                average_response_time = total_seconds / len(response_times)
            except ZeroDivisionError :
                average_response_time = 0  
            instance.vendor.average_response_time = average_response_time
            instance.vendor.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"acknowledgment_date":["acknowledgment_date can't be null"]}, status=status.HTTP_400_BAD_REQUEST)

