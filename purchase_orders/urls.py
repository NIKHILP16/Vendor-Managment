# vendor_app/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('', PurchaseOrderListCreateView.as_view(), name='purchase-order-list-create'),
    path('<uuid:pk>/', PurchaseOrderRetrieveUpdateDeleteView.as_view(), name='purchase-order-retrieve-update-delete'),
    path('<uuid:pk>/acknowledge', AcknowledgePurchaseOrderView.as_view(), name='acknowledge-purchase-order'),
]
