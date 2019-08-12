from django.conf.urls import url, include
from django.contrib import admin
from test_app import views as test_app_views
from main import views as main_views
from movie import views as movie_views
from ticket import views as ticket_views
from login import views as login_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.staticfiles.urls import static
from django.conf import settings
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

admin.site.site_header = '서울 시네마 관리자 페이지입니다'
admin.site.site_title = 'SEOUL CINEMA'
# admin.site.site_url = 'http://coffeehouse.com/'
admin.site.index_title = 'SEOUL CINEMA IN KOREA'
admin.empty_value_display = "'**Empty**"

urlpatterns = [
    #좌석정보 입력하는 테이블은 아예 admin 페이지 외부로 옮김
    url(r'^admin/seat_check/$',  movie_views.seat_check, name='seat_check'),
    #url(r'^admin/movie_schd/$',  movie_views.movie_schd, name='movie_schd'),
    url(r'^admin/movie_schd/$',  movie_views.movie_schd_daily, name='movie_schd_daily'),
    url(r'^admin/movie_now/$',  movie_views.movie_now, name='movie_now'),
    
    url(r'^admin/', admin.site.urls),
    url(r'^$', main_views.index),
    url(r'^movie/', include('movie.urls')),
    url(r'^ticket/', include('ticket.urls')),
    url(r'^test_app/', include('test_app.urls')),
    url(r'^login/', include('login.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^login/', include('django.contrib.auth.urls')),
    url(r'^make_accounts', login_views.make_accounts),
    url(r'^nonmember_temp_account', login_views.nonmember_temp_account),
    url(r'^nonlogin_check_reservation', login_views.nonlogin_check_reservation),

]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
