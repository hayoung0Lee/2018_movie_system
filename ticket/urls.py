from django.conf.urls import url
from ticket import views


urlpatterns = [
    url(r'^index/$', views.index),
    url(r'^(?P<pk>[0-9]+)/$', views.index_pk),
    url(r'^(?P<pk>[0-9]+)/(?P<pk_date>[0-9]+)/$', views.index_pk_date),
    url(r'^timetable/$', views.timetable),
    url(r'^timetable/(?P<pk_date>[0-9]+)/$', views.timetable_date),
    url(r'^guide/$', views.guide),
    url(r'^book/(?P<pk_movie>[0-9]+)/(?P<pk_schd>[0-9]+)$', views.ticket),
    url(r'^pay/(?P<pk_schd>[0-9]+)/(?P<pk_tickets>[a-zA-Z0-9]+)$', views.ticket_pay),
    url(r'^pay/card/(?P<amount_price>[0-9]+)/(?P<telcard_num>[0-9]+)$', views.card_pay),
    url(r'^pay/phone/(?P<amount_price>[0-9]+)/(?P<telcard_num>[0-9]+)$', views.phone_pay),
    url(r'^pay/done$', views.ticket_done, name='ticket_done'),
    url(r'^ajax/pay$', views.ajax_pay, name='ajax_pay'),
]