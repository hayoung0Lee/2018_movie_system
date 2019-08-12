from django.conf.urls import url
from movie import views


urlpatterns = [
    url(r'^post/detail/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/delete/$', views.post_delete, name='post_delete'),
    url(r'^post/show/(?P<pk>[0-9]+)/$', views.post_show, name='post_show'),
    #url(r'^post/error/$', views.movie_schd_daily, name='movie_schd_daily'),
    #url(r'^post/(?P<pk>\d+)/detail/$', views.post_detail, name='post_detail'),
    #상영일정 관련
    url(r'^schd/daily/$', views.movie_schd_daily, name='movie_schd_daily'),

    url(r'^ajax/validate_username/$', views.validate_username, name='validate_username'),
    url(r'^ajax/search_schd/$', views.search_schd, name='search_schd'),
    
    url(r'^$', views.index),
    url(r'^yet/$', views.movie_yet),
    url(r'^detail/(?P<pram_movie_no>.+)/$', views.movie_detail),
]
