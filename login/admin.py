from django.contrib import admin

# Register your models here.
#모듈을 Admin모듈과 연동하기 위한 설정
from .models import Customer, PointHistory# 현재앱의 model에서 customer table을 가져다 쓰겠다

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_id','customer_name','member_check','email','dob')
    search_fields = ('customer_id','member_check')
    ordering = ('customer_id',)


class PointHistoryAdmin(admin.ModelAdmin):
    list_display = ('customer_id','usage_date','usage_history_tag','rest_point_tag')
    search_fields = ('customer_id','usage_date')
    ordering = ('usage_date',)

    def usage_history_tag(self, obj) :
        return obj.usage_history

    def rest_point_tag(self, obj) :
        return obj.rest_point


    usage_history_tag.short_description = '포인트 내역'
    rest_point_tag.short_description = '잔여 포인트'

admin.site.register(Customer, CustomerAdmin)#customer table
admin.site.register(PointHistory, PointHistoryAdmin)#customer table
