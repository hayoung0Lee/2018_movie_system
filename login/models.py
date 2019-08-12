from __future__ import unicode_literals

from django.db import models
#from django.utils import timezone
# Create your models here.
#여기에 table만들기 모듈에서 사용할 DB model정의
class Customer(models.Model):
    customer_id = models.CharField(primary_key=True,max_length=50)
    customer_name = models.CharField(max_length=50, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    contact = models.CharField(max_length=13, blank=True, null=True)
    pwd = models.CharField(max_length=15, blank=True, null=True)
#    pwd = models.PasswordField(max_length=15, blank=True, null=True)
    member_check = models.CharField(max_length=1, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Customer'

    def __str__(self):# 이 class를 표현할 때 어떻게 표현할지
        return self.customer_name  #본인행의 값들중 customer_id(항목을 대표하는 이름)로 각 행마다를 표현한다
        #return '%d %s' % (self.customer_id, self.customer_name)


class PointHistory(models.Model):
    customer_id = models.ForeignKey(Customer, models.DO_NOTHING, db_column='customer_id', primary_key=True)
    usage_date = models.DateTimeField(primary_key=True, auto_now_add=True)
    usage_history = models.IntegerField(primary_key=True)
    rest_point = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'point_history'
        unique_together = ('customer_id', 'usage_date', 'usage_history')
