from django.contrib import admin
from .models import *

# Register your models here.



class PurchaseOrderTable(admin.ModelAdmin):
    list_display=('id','po_number','vendor','order_date','delivery_date','delivered_data','items','quantity','status','quality_rating','issue_date')
admin.site.register(PurchaseOrder,PurchaseOrderTable)    




