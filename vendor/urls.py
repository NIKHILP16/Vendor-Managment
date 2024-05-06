# vendor_app/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('', VendorListCreateView.as_view(), name='vendor-list-create'),
    path('<uuid:pk>/', VendorRetrieveUpdateDeleteView.as_view(), name='vendor-retrieve-update-delete'),
    path('<uuid:pk>/performance/', VendorPerformanceView.as_view(), name='vendor-performance'),
]
