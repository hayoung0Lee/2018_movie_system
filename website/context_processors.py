from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.text import capfirst


IGNORE_MODELS = (
    'auth',
    "sites",
    "sessions",
    "admin",
    "contenttypes",
)


def gnb_menus(request):
    menus = [
        {
            'name': 'HOME',
            'url': '/admin/',
        },
        {
            'name': 'MOVIES',
            'sub_menus': [
                {'name': '영화 관리', 'url': '/admin/movie/movie/'},
                {'name': '상영 등급 관리', 'url': '/admin/movie/scrnclass/'},
                #다른페이지로 링크 거는방법 screnenclass_status페이지로 넘어가는 방법
                #screenclass_status.html참고하기
                #{'name': '상영 등급 관리', 'url': '/admin/movie/screenclass/status/'},
            ]
        },
        {
            'name': 'SCHEDULES',
            'sub_menus': [
                #{'name': '상영 등급 관리', 'url': '/admin/movie/screenclass/status/'},
                #{'name': '현재 상영 일정', 'url': '/admin/movie_now/'},
                {'name': '상영 일정 등록', 'url': '/admin/movie_schd/'},
                {'name': '상영 일정 조회', 'url': '/admin/ticket/scrnschd/'},
            ]
        },
        {
            'name': 'THEATER',
            'sub_menus': [
                {'name': '상영관 관리', 'url': '/admin/movie/theater/'},
                {'name': '좌석 관리', 'url': '/admin/seat_check/'},
                #{'name': '좌석 관리', 'url': '/admin/movie/seats/'},
            ]
        },
        {
            'name': 'MEMBERS',
            'sub_menus': [
                {'name': '회원 관리', 'url': '/admin/login/customer/'},
                {'name': '포인트 관리', 'url': '/admin/login/pointhistory'},
                {'name': '예매 관리', 'url': '/admin/ticket/pay'},
                {'name': '할인 관리', 'url': '/admin/ticket/discount'},
            ]
        },

    ]
    return {'gnb_menus': menus}


def gnb_apps(request):
    user = request.user
    apps = []
    app_dict = {}
    for model, model_admin in admin.site._registry.items():
        app_label = model._meta.app_label

        if app_label in IGNORE_MODELS:
            continue

        has_module_perms = user.has_module_perms(app_label)

        if has_module_perms:
            perms = model_admin.get_model_perms(request)

            if True in perms.values():
                model_dict = {
                    'name': capfirst(model._meta.verbose_name_plural),
                    'admin_url': mark_safe('/admin/%s/%s/' % (app_label, model.__name__.lower())),
                    'perms': perms,
                }
                if app_label in app_dict:
                    app_dict[app_label]['models'].append(model_dict)
                else:
                    app_dict[app_label] = {
                        'app_label': app_label,
                        'name': app_label.title(),
                        'app_url': app_label + '/',
                        'has_module_perms': has_module_perms,
                        'models': [model_dict],
                    }

    for key in sorted(app_dict.keys()):
        apps.append(app_dict[key])

    return {'gnb_apps': apps}
