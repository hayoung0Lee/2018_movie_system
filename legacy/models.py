# # This is an auto-generated Django model module.
# # You'll have to do the following manually to clean this up:
# #   * Rearrange models' order
# #   * Make sure each model has one field with primary_key=True
# #   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
# #   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# # Feel free to rename the models, but don't rename db_table values or field names.
# from __future__ import unicode_literals
#
# from django.db import models
#
#
# class AccountPay(models.Model):
#     account_no = models.CharField(max_length=20, blank=True, null=True)
#     book_no = models.ForeignKey('Pay', models.DO_NOTHING, db_column='book_no', primary_key=True)
#
#     class Meta:
#         managed = False
#         db_table = 'account_pay'
#
#
# class AuthGroup(models.Model):
#     id = models.IntegerField(primary_key=True)  # AutoField?
#     name = models.CharField(unique=True, max_length=80, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_group'
#
#
# class AuthGroupPermissions(models.Model):
#     id = models.IntegerField(primary_key=True)  # AutoField?
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#     permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_group_permissions'
#         unique_together = (('group', 'permission'),)
#
#
# class AuthPermission(models.Model):
#     id = models.IntegerField(primary_key=True)  # AutoField?
#     name = models.CharField(max_length=255, blank=True, null=True)
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
#     codename = models.CharField(max_length=100, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_permission'
#         unique_together = (('content_type', 'codename'),)
#
#
# class AuthUser(models.Model):
#     id = models.IntegerField(primary_key=True)  # AutoField?
#     password = models.CharField(max_length=128, blank=True, null=True)
#     last_login = models.DateTimeField(blank=True, null=True)
#     is_superuser = models.BooleanField()
#     username = models.CharField(unique=True, max_length=150, blank=True, null=True)
#     first_name = models.CharField(max_length=30, blank=True, null=True)
#     last_name = models.CharField(max_length=30, blank=True, null=True)
#     email = models.CharField(max_length=254, blank=True, null=True)
#     is_staff = models.BooleanField()
#     is_active = models.BooleanField()
#     date_joined = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'auth_user'
#
#
# class AuthUserGroups(models.Model):
#     id = models.IntegerField(primary_key=True)  # AutoField?
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_user_groups'
#         unique_together = (('user', 'group'),)
#
#
# class AuthUserUserPermissions(models.Model):
#     id = models.IntegerField(primary_key=True)  # AutoField?
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_user_user_permissions'
#         unique_together = (('user', 'permission'),)
#
#
# class CardPay(models.Model):
#     approval_no = models.CharField(max_length=10, blank=True, null=True)
#     book_no = models.ForeignKey('Pay', models.DO_NOTHING, db_column='book_no', primary_key=True)
#
#     class Meta:
#         managed = False
#         db_table = 'card_pay'
#
#
# class Customer(models.Model):
#     customer_id = models.CharField(primary_key=True, max_length=50)
#     customer_name = models.CharField(max_length=50, blank=True, null=True)
#     dob = models.DateField(blank=True, null=True)
#     contact = models.CharField(max_length=13, blank=True, null=True)
#     pwd = models.CharField(max_length=15, blank=True, null=True)
#     member_check = models.CharField(max_length=1, blank=True, null=True)
#     email = models.CharField(max_length=50, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'customer'
#
#
# class Discount(models.Model):
#     telcard_no = models.CharField(primary_key=True, max_length=2)
#     telcard_name = models.CharField(max_length=50, blank=True, null=True)
#     discount_money = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'discount'
#
#
# class DjangoAdminLog(models.Model):
#     id = models.IntegerField(primary_key=True)  # AutoField?
#     action_time = models.DateTimeField()
#     object_id = models.TextField(blank=True, null=True)
#     object_repr = models.CharField(max_length=200, blank=True, null=True)
#     action_flag = models.IntegerField()
#     change_message = models.TextField(blank=True, null=True)
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'django_admin_log'
#
#
# class DjangoContentType(models.Model):
#     id = models.IntegerField(primary_key=True)  # AutoField?
#     app_label = models.CharField(max_length=100, blank=True, null=True)
#     model = models.CharField(max_length=100, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'django_content_type'
#         unique_together = (('app_label', 'model'),)
#
#
# class DjangoMigrations(models.Model):
#     id = models.IntegerField(primary_key=True)  # AutoField?
#     app = models.CharField(max_length=255, blank=True, null=True)
#     name = models.CharField(max_length=255, blank=True, null=True)
#     applied = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'django_migrations'
#
#
# class DjangoSession(models.Model):
#     session_key = models.CharField(primary_key=True, max_length=40)
#     session_data = models.TextField(blank=True, null=True)
#     expire_date = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'django_session'
#
#
# class Movie(models.Model):
#     class_no = models.ForeignKey('ScrnClass', models.DO_NOTHING, db_column='class_no')
#     movie_no = models.CharField(primary_key=True, max_length=4)
#     movie_name = models.CharField(max_length=50, blank=True, null=True)
#     scrn_date = models.DateField(blank=True, null=True)
#     genre = models.CharField(max_length=100, blank=True, null=True)
#     scrn_time = models.IntegerField(blank=True, null=True)
#     dist_name = models.CharField(max_length=50, blank=True, null=True)
#     director_name = models.CharField(max_length=50, blank=True, null=True)
#     actor_name = models.CharField(max_length=50, blank=True, null=True)
#     poster = models.CharField(max_length=100, blank=True, null=True)
#     trailer = models.CharField(max_length=100, blank=True, null=True)
#     movie_intro = models.CharField(max_length=700, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'movie'
#
#
# class Pay(models.Model):
#     pay_money = models.IntegerField(blank=True, null=True)
#     pay_way = models.CharField(max_length=2, blank=True, null=True)
#     pay_date = models.DateField(blank=True, null=True)
#     telcard_no = models.ForeignKey(Discount, models.DO_NOTHING, db_column='telcard_no', blank=True, null=True)
#     customer = models.ForeignKey(Customer, models.DO_NOTHING)
#     issue_check = models.CharField(max_length=1, blank=True, null=True)
#     book_no = models.CharField(primary_key=True, max_length=11)
#     usage_point = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'pay'
#
#
# class PhonePay(models.Model):
#     book_no = models.ForeignKey(Pay, models.DO_NOTHING, db_column='book_no', primary_key=True)
#     phone_no = models.CharField(max_length=13, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'phone_pay'
#
#
# class PointHistory(models.Model):
#     usage_history = models.IntegerField(primary_key=True)
#     usage_date = models.DateField()
#     rest_point = models.IntegerField()
#     customer = models.ForeignKey(Customer, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'point_history'
#         unique_together = (('usage_history', 'usage_date', 'customer'),)
#
#
# class ScrnClass(models.Model):
#     class_name = models.CharField(max_length=50, blank=True, null=True)
#     class_no = models.CharField(primary_key=True, max_length=2)
#
#     class Meta:
#         managed = False
#         db_table = 'scrn_class'
#
#
# class ScrnSchd(models.Model):
#     scrn_schd_no = models.CharField(primary_key=True, max_length=8)
#     theater_no = models.ForeignKey('Theater', models.DO_NOTHING, db_column='theater_no')
#     scrn_date = models.DateField(blank=True, null=True)
#     scrn_ep = models.IntegerField(blank=True, null=True)
#     start_time = models.DateField(blank=True, null=True)
#     end_time = models.DateField(blank=True, null=True)
#     movie_no = models.ForeignKey(Movie, models.DO_NOTHING, db_column='movie_no')
#
#     class Meta:
#         managed = False
#         db_table = 'scrn_schd'
#
#
# class Seat(models.Model):
#     seat_no = models.CharField(max_length=3)
#     theater_no = models.ForeignKey('Theater', models.DO_NOTHING, db_column='theater_no', primary_key=True)
#
#     class Meta:
#         managed = False
#         db_table = 'seat'
#         unique_together = (('theater_no', 'seat_no'),)
#
#
# class TestAppResource(models.Model):
#     id = models.IntegerField(primary_key=True)  # AutoField?
#     name = models.CharField(unique=True, max_length=80, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'test_app_resource'
#
#
# class Theater(models.Model):
#     theater_no = models.CharField(primary_key=True, max_length=2)
#     theater_name = models.CharField(max_length=50, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'theater'
#
#
# class Ticket(models.Model):
#     ticket_no = models.CharField(primary_key=True, max_length=11)
#     book_avail_check = models.CharField(max_length=1)
#     seat_no = models.ForeignKey(Seat, models.DO_NOTHING, db_column='seat_no')
#     theater_no = models.ForeignKey(Seat, models.DO_NOTHING, db_column='theater_no')
#     scrn_schd_no = models.ForeignKey(ScrnSchd, models.DO_NOTHING, db_column='scrn_schd_no')
#
#     class Meta:
#         managed = False
#         db_table = 'ticket'
#
#
# class TicketInfo(models.Model):
#     ticket_no = models.ForeignKey(Ticket, models.DO_NOTHING, db_column='ticket_no', primary_key=True)
#     book_no = models.ForeignKey(Pay, models.DO_NOTHING, db_column='book_no')
#
#     class Meta:
#         managed = False
#         db_table = 'ticket_info'
#         unique_together = (('ticket_no', 'book_no'),)
