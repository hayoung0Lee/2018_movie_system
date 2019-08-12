from django.contrib import admin
from django.utils.html import format_html
from django.conf import settings
from django.utils.safestring import mark_safe
# Register your models here.

# Register your models here.
from .models import Movie, ScrnClass
from .models import Theater, Seat
from django.conf.urls import url
from django.template.response import TemplateResponse
from django.shortcuts import render
from django.core.urlresolvers import reverse
# from post.filters import CreatedDateFilter
# from post.forms import MyPostAdminForm



'''
커스터마이징해서 어드민 페이지에 보이게 하는 방법
class ResourceAdmin(admin.ModelAdmin):
    list_display = ('id','name')

admin.site.register(Resource, ResourceAdmin)
'''
####movie 시작
class MovieAdmin(admin.ModelAdmin):
    list_display = ('movie_no','movie_name', 'poster_tag','scrn_date')
    #list_filter = ('movie_no',)
    search_fields = ('movie_name', 'director_name')
    list_per_page = 25


    def poster_tag(self, obj):
        #return str(obj.image).strip()
        #return format_html('<img src='+ "{}".format(obj.image.text).strip() + '/>')
        return mark_safe('<img src="{url}" width="{width}" />'.format(
            #url = 'post_image/test3.jpg',
            url = obj.poster.url,
            width= '300px',
            ))
    poster_tag.short_description = 'poster'



    # def get_urls(self):
    #     urls = super(MovieAdmin, self).get_urls()
    #     post_urls = [
    #         url(r'^status/$', self.admin_site.admin_view(self.movie_status_view))
    #     ]
    #     return post_urls + urls

    # def movie_status_view(self, request):
    #     context = dict(
    #         self.admin_site.each_context(request),
    #         movies=Movie.objects.all()
    #     )
    #     return TemplateResponse(request, "admin/movie_status.html", context)





class ScrnClassAdmin(admin.ModelAdmin):
    list_display = ('class_no','class_name')
    #list_filter = ('movie_no',)
    # search_fields = ('class_name',)
    list_per_page = 10

    def get_urls(self):
        urls = super(ScrnClassAdmin, self).get_urls()
        post_urls = [
            url(r'^status/$', self.admin_site.admin_view(self.scrnclass_status_view))
        ]
        return post_urls + urls

    def scrnclass_status_view(self, request):
        context = dict(
            self.admin_site.each_context(request),
            scrnclasses=ScrnClass.objects.all()
        )
        return TemplateResponse(request, "admin/scrnclass_status.html", context)


#기본
admin.site.register(Movie, MovieAdmin)
admin.site.register(ScrnClass, ScrnClassAdmin)



###movie끝

###상영관 관리 시작

class TheaterAdmin(admin.ModelAdmin):
    list_display = ('theater_no', 'theater_name',)
    search_fields = ('theater_name',)
    ordering = ('theater_no',)
    #def detail_tag(self, obj):
    #     #return str(obj.image).strip()
    #     #return format_html('<img src='+ "{}".format(obj.image.text).strip() + '/>')
        #return mark_safe('<a href="index.html">좌석 정보 수정하기</>')
        #return mark_safe('<a href="/admin/movie/seat/status/'+objo>좌석 정보 수정하기</>')
    #     #return mark_safe('<a href="../../ttt.html">좌석 정보 수정하기</>')
    #     #return mark_safe('<a href="{% url'+admin:index+' %}">좌석 정보 수정하기</>')




    #
    # def get_urls(self):
    #     urls = super(SeatAdmin, self).get_urls()
    #     post_urls = [
    #         url(r'^status/$', self.admin_site.admin_view(self.seat_status_view))
    #     ]
    #     return post_urls + urls
    #
    # def seat_status_view(self, request):
    #     context = dict(
    #         self.admin_site.each_context(request),
    #         seats=Seat.objects.all()
    #     )
    #     return TemplateResponse(request, "admin/seat_status.html", context)


class SeatAdmin(admin.ModelAdmin):
    list_display = ('seat_no',)
    #list_filter = ('movie_no',)


#기본
admin.site.register(Theater, TheaterAdmin)
admin.site.register(Seat, SeatAdmin)
###상영관 관리 끝
