from django.db import models
from movie.models import Movie, Theater, Seat, ScrnClass
from login.models import Customer
import datetime

class ScrnSchd(models.Model):
    scrn_schd_no = models.CharField(primary_key=True, max_length=20, blank=True, null=True)
    movie_no = models.ForeignKey(Movie, db_column='movie_no')
    theater_no = models.ForeignKey(Theater, models.DO_NOTHING, db_column='theater_no')
    scrn_date = models.DateField(blank=True, null=True) #yyddmm
    scrn_ep = models.CharField(max_length=3, blank=True, null=True)
    start_time = models.TimeField(blank=True, null=True, choices=(
        (datetime.datetime.strptime('6:00 am', "%I:%M %p").time(), '6:00 am'),
        (datetime.datetime.strptime('6:30 am', "%I:%M %p").time(), '6:30 am'),
        (datetime.datetime.strptime('7:00 am', "%I:%M %p").time(), '7:00 am'),
        (datetime.datetime.strptime('7:30 am', "%I:%M %p").time(), '7:30 am'),
        (datetime.datetime.strptime('8:00 am', "%I:%M %p").time(), '8:00 am'),
        (datetime.datetime.strptime('8:30 am', "%I:%M %p").time(), '8:30 am'),
        (datetime.datetime.strptime('9:00 am', "%I:%M %p").time(), '9:00 am'),
        (datetime.datetime.strptime('9:30 am', "%I:%M %p").time(), '9:30 am'),
        (datetime.datetime.strptime('10:00 am', "%I:%M %p").time(), '10:00 am'),
        (datetime.datetime.strptime('10:30 am', "%I:%M %p").time(), '10:30 am'),
        (datetime.datetime.strptime('11:00 am', "%I:%M %p").time(), '11:00 am'),
        (datetime.datetime.strptime('11:30 am', "%I:%M %p").time(), '11:30 am'),
        (datetime.datetime.strptime('12:00 pm', "%I:%M %p").time(), '12:00 pm'),
        (datetime.datetime.strptime('12:30 pm', "%I:%M %p").time(), '12:30 pm'),
        (datetime.datetime.strptime('1:00 pm', "%I:%M %p").time(), '1:00 pm'),
        (datetime.datetime.strptime('1:30 pm', "%I:%M %p").time(), '1:30 pm'),
        (datetime.datetime.strptime('2:00 pm', "%I:%M %p").time(), '2:00 pm'),
        (datetime.datetime.strptime('2:30 pm', "%I:%M %p").time(), '2:30 pm'),
        (datetime.datetime.strptime('3:00 pm', "%I:%M %p").time(), '3:00 pm'),
        (datetime.datetime.strptime('3:30 pm', "%I:%M %p").time(), '3:30 pm'),
        (datetime.datetime.strptime('4:00 pm', "%I:%M %p").time(), '4:00 pm'),
        (datetime.datetime.strptime('4:30 pm', "%I:%M %p").time(), '4:30 pm'),
        (datetime.datetime.strptime('5:00 pm', "%I:%M %p").time(), '5:00 pm'),
        (datetime.datetime.strptime('5:30 pm', "%I:%M %p").time(), '5:30 pm'),
        (datetime.datetime.strptime('6:00 pm', "%I:%M %p").time(), '6:00 pm'),
        (datetime.datetime.strptime('6:30 pm', "%I:%M %p").time(), '6:30 pm'),
        (datetime.datetime.strptime('7:00 pm', "%I:%M %p").time(), '7:00 pm'),
        (datetime.datetime.strptime('7:30 pm', "%I:%M %p").time(), '7:30 pm'),
        (datetime.datetime.strptime('8:00 pm', "%I:%M %p").time(), '8:00 pm'),
        (datetime.datetime.strptime('8:30 pm', "%I:%M %p").time(), '8:30 pm'),
        (datetime.datetime.strptime('9:00 pm', "%I:%M %p").time(), '9:00 pm'),
        (datetime.datetime.strptime('9:30 pm', "%I:%M %p").time(), '9:30 pm'),
        (datetime.datetime.strptime('10:00 pm', "%I:%M %p").time(), '10:00 pm'),
        (datetime.datetime.strptime('10:30 pm', "%I:%M %p").time(), '10:30 pm'),
        (datetime.datetime.strptime('11:00 pm', "%I:%M %p").time(), '11:00 pm'),
        (datetime.datetime.strptime('11:30 pm', "%I:%M %p").time(), '11:30 pm'),
        (datetime.datetime.strptime('12:00 am', "%I:%M %p").time(), '12:00 am'),
        (datetime.datetime.strptime('12:30 am', "%I:%M %p").time(), '12:30 am'),
        (datetime.datetime.strptime('01:00 am', "%I:%M %p").time(), '01:00 am'),
        (datetime.datetime.strptime('01:30 am', "%I:%M %p").time(), '01:30 am'),
        (datetime.datetime.strptime('02:00 am', "%I:%M %p").time(), '02:00 am'),
        (datetime.datetime.strptime('02:30 am', "%I:%M %p").time(), '02:30 am'),
    )) #hhmm(24시간)
    end_time = models.TimeField(blank=True, null=True, choices=(
        (datetime.datetime.strptime('6:00 am', "%I:%M %p").time(), '6:00 am'),
        (datetime.datetime.strptime('6:30 am', "%I:%M %p").time(), '6:30 am'),
        (datetime.datetime.strptime('7:00 am', "%I:%M %p").time(), '7:00 am'),
        (datetime.datetime.strptime('7:30 am', "%I:%M %p").time(), '7:30 am'),
        (datetime.datetime.strptime('8:00 am', "%I:%M %p").time(), '8:00 am'),
        (datetime.datetime.strptime('8:30 am', "%I:%M %p").time(), '8:30 am'),
        (datetime.datetime.strptime('9:00 am', "%I:%M %p").time(), '9:00 am'),
        (datetime.datetime.strptime('9:30 am', "%I:%M %p").time(), '9:30 am'),
        (datetime.datetime.strptime('10:00 am', "%I:%M %p").time(), '10:00 am'),
        (datetime.datetime.strptime('10:30 am', "%I:%M %p").time(), '10:30 am'),
        (datetime.datetime.strptime('11:00 am', "%I:%M %p").time(), '11:00 am'),
        (datetime.datetime.strptime('11:30 am', "%I:%M %p").time(), '11:30 am'),
        (datetime.datetime.strptime('12:00 pm', "%I:%M %p").time(), '12:00 pm'),
        (datetime.datetime.strptime('12:30 pm', "%I:%M %p").time(), '12:30 pm'),
        (datetime.datetime.strptime('1:00 pm', "%I:%M %p").time(), '1:00 pm'),
        (datetime.datetime.strptime('1:30 pm', "%I:%M %p").time(), '1:30 pm'),
        (datetime.datetime.strptime('2:00 pm', "%I:%M %p").time(), '2:00 pm'),
        (datetime.datetime.strptime('2:30 pm', "%I:%M %p").time(), '2:30 pm'),
        (datetime.datetime.strptime('3:00 pm', "%I:%M %p").time(), '3:00 pm'),
        (datetime.datetime.strptime('3:30 pm', "%I:%M %p").time(), '3:30 pm'),
        (datetime.datetime.strptime('4:00 pm', "%I:%M %p").time(), '4:00 pm'),
        (datetime.datetime.strptime('4:30 pm', "%I:%M %p").time(), '4:30 pm'),
        (datetime.datetime.strptime('5:00 pm', "%I:%M %p").time(), '5:00 pm'),
        (datetime.datetime.strptime('5:30 pm', "%I:%M %p").time(), '5:30 pm'),
        (datetime.datetime.strptime('6:00 pm', "%I:%M %p").time(), '6:00 pm'),
        (datetime.datetime.strptime('6:30 pm', "%I:%M %p").time(), '6:30 pm'),
        (datetime.datetime.strptime('7:00 pm', "%I:%M %p").time(), '7:00 pm'),
        (datetime.datetime.strptime('7:30 pm', "%I:%M %p").time(), '7:30 pm'),
        (datetime.datetime.strptime('8:00 pm', "%I:%M %p").time(), '8:00 pm'),
        (datetime.datetime.strptime('8:30 pm', "%I:%M %p").time(), '8:30 pm'),
        (datetime.datetime.strptime('9:00 pm', "%I:%M %p").time(), '9:00 pm'),
        (datetime.datetime.strptime('9:30 pm', "%I:%M %p").time(), '9:30 pm'),
        (datetime.datetime.strptime('10:00 pm', "%I:%M %p").time(), '10:00 pm'),
        (datetime.datetime.strptime('10:30 pm', "%I:%M %p").time(), '10:30 pm'),
        (datetime.datetime.strptime('11:00 pm', "%I:%M %p").time(), '11:00 pm'),
        (datetime.datetime.strptime('11:30 pm', "%I:%M %p").time(), '11:30 pm'),
        (datetime.datetime.strptime('12:00 am', "%I:%M %p").time(), '12:00 am'),
        (datetime.datetime.strptime('12:30 am', "%I:%M %p").time(), '12:30 am'),
        (datetime.datetime.strptime('01:00 am', "%I:%M %p").time(), '01:00 am'),
        (datetime.datetime.strptime('01:30 am', "%I:%M %p").time(), '01:30 am'),
        (datetime.datetime.strptime('02:00 am', "%I:%M %p").time(), '02:00 am'),
        (datetime.datetime.strptime('02:30 am', "%I:%M %p").time(), '02:30 am'),
    ))  #hhmm(24시간)

    class Meta:
        managed = False
        db_table = 'scrn_schd'

    def __str__(self):
        return str(self.movie_no) + '의 ' + str(self.scrn_date) + '일 ' + str(self.theater_no) +' ' + str(self.scrn_ep) + '회차 '+ str(self.start_time)+'시 상영일정이 등록되었습니다.'


class Ticket(models.Model):
    ticket_no = models.CharField(primary_key=True, max_length=11)
    book_avail_check = models.CharField(max_length=1, blank=True, null=True)
    seat_no = models.ForeignKey(Seat, models.DO_NOTHING, db_column='seat_no',related_name = 'seat_no_content_type')
    theater_no = models.ForeignKey(Seat, models.DO_NOTHING, db_column='theater_no',related_name = 'theater_no_content_type')
    scrn_schd_no = models.ForeignKey(ScrnSchd, models.DO_NOTHING, db_column='scrn_schd_no', related_name = 'scrn_schd_no_content_type')

    class Meta:
        managed = False
        db_table = 'ticket'


class Discount(models.Model):
    telcard_no = models.CharField(primary_key=True, max_length=2)
    telcard_name = models.CharField(max_length=50, blank=True, null=True)
    discount_money = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discount'


class Pay(models.Model):
    book_no = models.CharField(primary_key=True, max_length=11)
    pay_money = models.IntegerField(blank=True, null=True)
    pay_way = models.CharField(max_length=2, blank=True, null=True)
    pay_date = models.DateField(blank=True, null=True)
    telcard_no = models.ForeignKey(Discount, models.DO_NOTHING, db_column='telcard_no', blank=False, null=False)
    customer_id = models.ForeignKey(Customer, models.DO_NOTHING, db_column='customer_id', blank=False, null=False)
    issue_check = models.CharField(max_length=1, blank=True, null=True)
    usage_point = models.IntegerField(blank=False, null=False)

    class Meta:
        managed = False
        db_table = 'pay'


class TicketInfo(models.Model):
     ticket_no = models.ForeignKey(Ticket, models.DO_NOTHING, db_column='ticket_no', primary_key=True)
     book_no = models.ForeignKey(Pay, models.DO_NOTHING, db_column='book_no', primary_key=True)

     class Meta:
         managed = False
         db_table = 'ticket_info'
         unique_together = ('ticket_no', 'book_no')


class CardPay(models.Model):
    approval_no = models.CharField(max_length=10, blank=True, null=True)
    book_no = models.ForeignKey(Pay, models.DO_NOTHING, db_column='book_no', primary_key=True)
    class Meta:
        managed = False
        db_table = 'card_pay'

class PhonePay(models.Model):
    book_no = models.ForeignKey(Pay, models.DO_NOTHING, db_column='book_no', primary_key=True)
    phone_no = models.CharField(max_length=13, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'phone_pay'


# class AccountPay(models.Model):
#     account_no = models.CharField(max_length=20, blank=True, null=True)
#     book_no = models.ForeignKey('Pay', models.DO_NOTHING, db_column='book_no', primary_key=True)
#
#     class Meta:
#         managed = False
#         db_table = 'account_pay'
#
#