from django.contrib import admin
from .models import *

# Register your models here.

class VendorTable(admin.ModelAdmin):
    list_display = ('id','user','name','contact_details','address','vendor_code','on_time_delivery_rate','quality_rating_avg','average_response_time','fulfillment_rate')
admin.site.register(Vendor,VendorTable)



class HistoricalPerformanceTable(admin.ModelAdmin):
    list_display = ('id','vendor','date','on_time_delivery_rate','quality_rating_avg','average_response_time','fulfillment_rate')
admin.site.register(HistoricalPerformance,HistoricalPerformanceTable)



