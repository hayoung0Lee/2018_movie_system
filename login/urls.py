from django.conf.urls import url, include
#from django.urls import path
#from test_app import views
#from . import views #as login_views
from login import views as login_views #as login_views 위의것과 동일?

from django.contrib.auth import views as auth_views
urlpatterns = [ #앞:주소, 뒤:누가 처리할지
    #url(r'^$', login_views.login_index),

    #url(r'^) 회원가입으로 연결되게
    #url() 로그인 성공시 화면으로(뭐보여주는지 찾아서 만들기)
    #여기 적어야하는거 찾기
    #url(r'^make_accounts', login_views.make_account_index)
    #url(r'^make_account/(?P<area>\d+)/$', login_view.make_account_index)
    #url(r'make_account/', login_views.make_account_index),<-이거 돌아간다(회원가입 페이지)

#    url(r'^login/$', auth_views.login, name='login'),


#    url(r'^accounts/', include('django.contrib.auth.urls')),#로그인폼
#    url(r'^login/$', auth_views.login, name='login'),

#    url(r'^login/$', auth_views.login, {'login': 'core\login.html'}, name='login'),
#    url(r'^accounts/', auth_views.login, {'login\login.html': 'core/login.html'}, name='login'),

#include : App에 대해 처리할때

#빈경로
    #url(r'^$', login_views.show_login_index, name='show_login_index'), #http://localhost:8000/login
    url(r'^$', auth_views.login),
    url(r'^../make_accounts', login_views.make_accounts, name = 'make_accounts'), #http://localhost:8000/login/make_accounts/
    url(r'^../nonmember_temp_account', login_views.nonmember_temp_account, name = 'nonmember_temp_account'),
    #회원가입 페이지
    url(r'^made_new_account', login_views.made_new_account, name='made_new_account'),
    url(r'^made_nonmember_account', login_views.made_nonmember_account, name='made_nonmember_account'),
    url(r'^try_login', login_views.try_login, name='try_login'),
    url(r'^logout/$', auth_views.logout, {'next_page':'/'}, name='logout'),
    url(r'^mypage', login_views.mypage, name = 'mypage'),
    url(r'^my_info', login_views.my_info, name = 'my_info'),
    url(r'^check_reservation', login_views.check_reservation, name = 'check_reservation'),
    url(r'^my_point', login_views.my_point, name = 'my_point'),
    url(r'^nonlogin_check_reservation', login_views.nonlogin_check_reservation, name = 'nonlogin_check_reservation'),


    #url(r'^temp_index', login_views.temp_index),
    #url(r'^user_mode', login_view.user_mode, name = 'user_mode'),



    #url(r'^done', login_views.make_accounts),
#    url(r'make_account/(?P<customers>)', login_views.make_accounts),

#    "make_accounts/{{customers}}

    #url(r'^logout/$', login_views.login_index, name='logout')

    #path('<int:question_id>/', views.detail, name='detail')

    #url(r'^logout/$', login_views.logged_out_test, {'next_page' : '/'}),
    #url(r'^login_test/$', login_views.make_account_test,  {'template_name':'memo_app/login.html'}),
]
#^login/$ [name='login']
#^logout/$ [name='logout']
#^password_change/$ [name='password_change']
#^password_change/done/$ [name='password_change_done']
#^password_reset/$ [name='password_reset']
#^password_reset/done/$ [name='password_reset_done']
#^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$ [name='password_reset_confirm']
#^reset/done/$ [name='password_reset_complete']


#url(r'^test_app/', include('test_app.urls')),