from django.contrib import admin
from .models import ScrnSchd,Ticket, Discount, Pay
from django.conf.urls import url
# Register your models here.

#
class ScrnSchdAdmin(admin.ModelAdmin):
    list_per_page = 15
    search_fields = ('scrn_date','start_time')
    ordering = ('scrn_date','start_time','scrn_ep')

class DiscountAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_display = ('telcard_no','telcard_name','discount_money')


class PayAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_display = ('book_no','customer_id','pay_way','pay_date')
    search_fields = ('book_no','customer_id','pay_way','pay_date')

admin.site.register(ScrnSchd,ScrnSchdAdmin)
admin.site.register(Ticket)
admin.site.register(Discount,DiscountAdmin)
admin.site.register(Pay,PayAdmin)