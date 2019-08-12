from django.shortcuts import render
from django.db.models import F, Sum, Count, Case, When
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core.exceptions import MultipleObjectsReturned
import datetime, time, json, random

from .models import *
from movie.models import Movie, Theater, Seat
from login.models import Customer, PointHistory

#영화별예매 첫페이지 - 영화선택하도록
def index(request):
    today_datetime = datetime.date.today()

    today_datetime = datetime.date.today()
    date = today_datetime

    if(date == today_datetime):
        msg = False
    else:
        msg = True
    schd_qs = ScrnSchd.objects.select_related('movie_no').filter(scrn_date__icontains = today_datetime) 

    #movie_no 목록을 중복 제거 하고 넘김
    #movie_select 부분에 들어가는 movies
    movies = set()
    for schd in schd_qs:
        movies.add(schd.movie_no)

    today = '{0}.{1} {2}'.format(today_datetime.month, today_datetime.day, week2string(today_datetime.weekday()))
    context = { 'movies':movies, 'date':today, 'today':today, 'msg':msg }
    return render(request, 'ticket_index.html', context)


#영화별예매 - 선택한 영화의 오늘 상영관별 시간표
def index_pk(request, pk):
    msg = '-pk page'
    today_datetime = datetime.date.today()
    date = today_datetime

    if(date == today_datetime):
        msg = False
    else:
        msg = True

    #오늘날짜의 해당 전체영화의 상영일정
    schd_qs = ScrnSchd.objects.select_related('movie_no').filter(scrn_date__icontains = today_datetime)
    #pk에 해당하는 movie
    pk_movie = Movie.objects.get(movie_no = pk)
    selected_movie = pk_movie

    #이전, 다음 날짜 설정
    prev_day = today_datetime - datetime.timedelta(days=1)
    next_day = today_datetime + datetime.timedelta(days=1)
    prev_day = prev_day.strftime('%y%m%d')
    next_day = next_day.strftime('%y%m%d')

    #movie_no 목록을 중복 제거 하고 넘김
    #movie_select 부분에 들어가는 movies
    movies = set()
    for schd in schd_qs:
        movies.add(schd.movie_no)

    #pk에 해당하는 영화의 오늘 날짜 상영관별 시간표
    schd_qs_pk = schd_qs.filter(movie_no__movie_no__icontains = pk)
    theater_set = set()
    schd_list = []
    for schd in schd_qs_pk:
        theater_set.add(schd.theater_no.theater_no)
    theater_list = list(theater_set)
    theater_list.sort()
    for theater_no in theater_list:
        schd_list.append(schd_qs_pk.filter(theater_no__theater_no__icontains = theater_no))
    
    date = '{0}.{1} {2}'.format(date.month, date.day, week2string(date.weekday()))
    today = '{0}.{1} {2}'.format(today_datetime.month, today_datetime.day, week2string(today_datetime.weekday())+'요일')
    context = { 'schd_list':schd_list , 'movies':movies, 'today':today, 'date':date, 'prev_day':prev_day, 'next_day':next_day, 'selected_movie':selected_movie, 'msg':msg }
    return render(request, 'ticket_index.html', context)

#영화별예매 - 선택한 영화의 선택한 날짜의 상영관별 시간표
def index_pk_date(request, pk, pk_date):
    msg = 'index_pk_date'
    #date 문자열 parsing
    date = datetime.date(int('20'+pk_date[0:2]), int(pk_date[2:4]), int(pk_date[4:6]))
    today_datetime = datetime.date.today()

    if(date == today_datetime):
        msg = False
    else:
        msg = True


    #오늘날짜의 해당 전체영화의 상영일정 //영화 선택 목록의 영화들은 항상 오늘 날짜에 상영하는 영화를 보여줌
    schd_qs = ScrnSchd.objects.select_related('movie_no').filter(scrn_date__icontains = today_datetime)
    #pk에 해당하는 movie
    pk_movie = Movie.objects.get(movie_no = pk)

    #이전, 다음 날짜 설정
    prev_day = date - datetime.timedelta(days=1)
    next_day = date + datetime.timedelta(days=1)
    prev_day = prev_day.strftime('%y%m%d')
    next_day = next_day.strftime('%y%m%d')

    #movie_no 목록을 중복 제거 하고 넘김
    #movie_select 부분에 들어가는 movies
    movies = set()
    for schd in schd_qs:
        movies.add(schd.movie_no)

    #해당날짜의 영화 목록
    schd_qs = ScrnSchd.objects.select_related('movie_no').filter(scrn_date__icontains = date) 

    #pk에 해당하는 영화의 오늘 날짜 상영관별 시간표
    schd_qs_pk = schd_qs.filter(movie_no__movie_no__icontains = pk)
    theater_set = set()
    schd_list = []
    for schd in schd_qs_pk:
        theater_set.add(schd.theater_no.theater_no)
    theater_list = list(theater_set)
    theater_list.sort()
    for theater_no in theater_list:
        schd_list.append(schd_qs_pk.filter(theater_no__theater_no__icontains = theater_no))

    selected_movie = pk_movie
    date = '{0}.{1} {2}'.format(date.month, date.day, week2string(date.weekday()))
    today = '{0}.{1} {2}'.format(today_datetime.month, today_datetime.day, week2string(today_datetime.weekday())+'요일')
    context = { 'schd_list':schd_list , 'movies':movies, 'today':today, 'date':date, 'prev_day':prev_day, 'next_day':next_day, 'selected_movie':selected_movie, 'msg':msg }
    return render(request, 'ticket_index.html', context)

#기본 상영시간표(today)
def timetable(request):

    today_datetime = datetime.date.today()
    schds_qs = ScrnSchd.objects.select_related('movie_no').filter(scrn_date__icontains = today_datetime) 

    #이전, 다음 날짜 설정
    prev_day = today_datetime - datetime.timedelta(days=1)
    next_day = today_datetime + datetime.timedelta(days=1)
    prev_day = prev_day.strftime('%y%m%d')
    next_day = next_day.strftime('%y%m%d')

    movie_no_set = set()
    movie_cnts = {}
    movie_cnt_list = []
    schd_list = []

    for schd in schds_qs:
        movie_cnt_list.append(schd.movie_no.movie_no)
    for schd in schds_qs:
        movie_no_set.add(schd.movie_no.movie_no)
    movie_no_list = list(movie_no_set)
    movie_no_list.sort()
    schd_list = []
    for movie_number in movie_no_list:
        schd_list.append(schds_qs.filter(movie_no__movie_no__icontains = movie_number))

    today = '{0}.{1} {2}'.format(today_datetime.month, today_datetime.day, week2string(today_datetime.weekday()))
    context = { 'schd_list':schd_list , 'date':today, 'prev_day':prev_day, 'next_day':next_day }
    return render(request, 'ticket_timetable.html', context)

#날짜별 상영시간표
def timetable_date(request, pk_date):

    #date 문자열 parsing
    date = datetime.date(int('20'+pk_date[0:2]), int(pk_date[2:4]), int(pk_date[4:6]))
    schds_qs = ScrnSchd.objects.select_related('movie_no').filter(scrn_date__icontains = date) 
    
    #이전, 다음 날짜 설정
    prev_day = date - datetime.timedelta(days=1)
    next_day = date + datetime.timedelta(days=1)
    prev_day = prev_day.strftime('%y%m%d')
    next_day = next_day.strftime('%y%m%d')

    movie_no_set = set()
    movie_cnts = {}
    movie_cnt_list = []
    schd_list = []

    for schd in schds_qs:
        movie_cnt_list.append(schd.movie_no.movie_no)
    for schd in schds_qs:
        movie_no_set.add(schd.movie_no.movie_no)
    movie_no_list = list(movie_no_set)
    movie_no_list.sort()
    schd_list = []
    for movie_number in movie_no_list:
        schd_list.append(schds_qs.filter(movie_no__movie_no__icontains = movie_number))

    date = '{0}.{1} {2}'.format(date.month, date.day, week2string(date.weekday()))
    context = { 'schd_list':schd_list , 'date':date, 'prev_day':prev_day, 'next_day':next_day }
    return render(request, 'ticket_timetable.html', context)

#예매 및 할인 가이드
def guide(request):
    msg = 'guide'
    context = { 'msg':msg  }
    return render(request, 'ticket_guide.html', context)

#예매 - 첫 페이지
def ticket(request, pk_movie, pk_schd):

    if request.session:
        print("ok")
    else:
        print("no")

    pk_schd = space_append(8, pk_schd)
    selected_movie = Movie.objects.get(movie_no = pk_movie)
    selected_schd = ScrnSchd.objects.get(scrn_schd_no = pk_schd)
    selected_schd.scrn_schd_no = selected_schd.scrn_schd_no.strip()
    
    #ticket_qs = Ticket.objects.filter(scrn_schd_no__scrn_schd_no__exact = pk_schd)
    print(selected_schd.theater_no.theater_no)
    ticket_qs = Ticket.objects.filter(theater_no__exact = selected_schd.theater_no.theater_no)
    #ticket_qs_filtered = ticket_qs.filter(theater_no__theater_no__exact = selected_schd.theater_no.theater_no)
    print("seletec.scrn_schd_no:", pk_schd, ":ss")
    ticket_qs_filtered = ticket_qs.filter(scrn_schd_no__scrn_schd_no__exact = pk_schd)
    t_qs = ticket_qs_filtered.filter(seat_no__theater_no__exact = selected_schd.theater_no.theater_no)

    ticket_list = []
    ticket_x_list = []
    for ticket in t_qs:
        print("ticket_no:", ticket.ticket_no)
        if ticket.book_avail_check == '0':
            print("book_avail_check")
            temp = (ticket.ticket_no)[9:11]
            print(temp)
            ticket_list.append(temp)
        else:
            print("else")
            temp = ticket.ticket_no[9:11]
            print(temp)
            ticket_x_list.append(temp)

    print("ticket_x_list:", ticket_x_list)
    print("ticket_list:", ticket_list)

    ticket_list = json.dumps(ticket_list)
    ticket_x_list = json.dumps(ticket_x_list)
    
    start_time = datetime.datetime(selected_schd.scrn_date.year, selected_schd.scrn_date.month, selected_schd.scrn_date.day, selected_schd.start_time.hour, selected_schd.start_time.minute, selected_schd.start_time.second)
    end_time = start_time + datetime.timedelta(minutes = selected_movie.scrn_time)

    date_obj = datetime.date(selected_schd.scrn_date.year, selected_schd.scrn_date.month, selected_schd.scrn_date.day)
    date = '{0}월 {1}일 {2}요일'.format(date_obj.month, date_obj.day, week2string(date_obj.weekday()))
    context = { 'selected_movie':selected_movie, 'selected_schd':selected_schd, 'date':date, 'start_time':start_time, 'end_time':end_time, 'ticket_list':ticket_list, 'ticket_x_list':ticket_x_list }
    return render(request, 'ticket_book.html', context)


#예매 - 결제 페이지
def ticket_pay(request, pk_schd, pk_tickets):
    if request.session['customer_id']:
        customer_id = request.session['customer_id']
    else:
        print("session error")

    ticket_price = 10000 #티켓 당 판매 가격
    pk_schd = space_append(8, pk_schd)

    ticket_schd_qs = Ticket.objects.filter(scrn_schd_no__scrn_schd_no__exact = pk_schd)
    discount_qs = Discount.objects.filter(telcard_no__startswith = '0')
    selected_schd = ScrnSchd.objects.get(scrn_schd_no = pk_schd)
    ticket_qs_list = []

    ticket_list = pk_tickets.split('n')
    del ticket_list[0]
    print(ticket_list)

    for ticket in ticket_list:
        ticket = space_append(3, ticket)
        ticket_qs_list.append(ticket_schd_qs.get(seat_no = ticket))

    #포인트 조회
    point_history_qs = PointHistory.objects.filter(customer_id__customer_id__exact = customer_id).order_by('usage_date').last()
    print(point_history_qs.rest_point)
    rest_point = point_history_qs.rest_point

    start_time = datetime.datetime(selected_schd.scrn_date.year, selected_schd.scrn_date.month, selected_schd.scrn_date.day, selected_schd.start_time.hour, selected_schd.start_time.minute, selected_schd.start_time.second)
    end_time = start_time + datetime.timedelta(minutes = selected_schd.movie_no.scrn_time)

    date_obj = datetime.date(selected_schd.scrn_date.year, selected_schd.scrn_date.month, selected_schd.scrn_date.day)
    date = '{0}월 {1}일 {2}요일'.format(date_obj.month, date_obj.day, week2string(date_obj.weekday()))

    price = len(ticket_list) * ticket_price

    context = { 'selected_schd':selected_schd, 'date':date, 'start_time':start_time, 'end_time':end_time, 'ticket_list':ticket_list,
    'price':price, 'ticket_qs_list':ticket_qs_list, 'discount_qs':discount_qs, 'rest_point':rest_point, 'customer_id':customer_id }
    return render(request, 'ticket_pay.html', context)
  

def ticket_done(request):
    context = {}
    return render(request, 'ticket_done.html', context)


def card_pay(request, amount_price, telcard_num):
    amount = amount_price
    telcard = str(telcard_num)[1]

    context = { 'amount':amount, 'telcard':telcard }
    return render(request, 'card_pay.html', context)


def phone_pay(request, amount_price, telcard_num):
    amount = amount_price
    telcard = telcard_num
    context = { 'amount':amount, 'telcard':telcard }
    return render(request, 'phone_pay.html', context)


@csrf_exempt
def ajax_pay(request):
    today = datetime.date.today()
    today_datetime = datetime.datetime.today()
    aprv_no = int(random.random()*10000)

    book_random_1 = int(random.random()*10000)
    book_random_1 = zero_append(4, str(book_random_1))
    book_random_2 = int(random.random()*10000)
    book_random_2 = zero_append(4, str(book_random_2))
    book_random_3 = int(random.random()*1000)
    book_random_3 = zero_append(3, str(book_random_3))

    print('pay_ajax')

    if request.method == 'POST':
        print('inside if statement')

        customer_id = request.POST.get('customer_id')
        telcard_no = request.POST.get('telcard_no')
        pay_money = request.POST.get('pay_money')
        pay_way = request.POST.get('pay_way')
        pay_date = today
        issue_check = '0'
        usage_point = request.POST.get('usage_point')
        ticket_list = request.POST.get('ticket_list')
        scrn_schd_no = request.POST.get('scrn_schd_no')

        print(customer_id)
        print(telcard_no)
        print(pay_money)
        print(pay_way)
        print(pay_date)
        print(issue_check)
        print(usage_point)
        print(ticket_list)

        customer_qs = Customer.objects.get(customer_id = customer_id)
        telcard_qs = Discount.objects.get(telcard_no = telcard_no)
        
        #pay table에 저장
        book_no = str(book_random_1) + str(book_random_2) + str(book_random_3)
        print(book_no)
        Pay.objects.create(book_no = book_no, customer_id = customer_qs, telcard_no = telcard_qs, pay_money = pay_money, pay_way = pay_way,
        pay_date = pay_date, issue_check = issue_check, usage_point = usage_point)
        book_no_qs = Pay.objects.get(book_no = book_no)

        #ticket_info에 저장
        seat_list = ticket_list.split(',')
        print(seat_list)

        ticket_qs_list = []
        for seat in seat_list:
            seat = space_append(3, seat)
            seat_qs = Ticket.objects.filter(seat_no__seat_no__exact = seat)
            seat_qs.update(book_avail_check = 1)
            ticket_qs_list.append(seat_qs.get(scrn_schd_no = scrn_schd_no))

        for ticket_qs in ticket_qs_list:
            TicketInfo.objects.create(ticket_no = ticket_qs, book_no = book_no_qs)

        #결제방법에 따른 정보 저장
        if (pay_way == '03'):
            print("phone")
            #휴대폰
            phone_no = request.POST.get('phone_no')
            PhonePay.objects.create(book_no = book_no_qs, phone_no = phone_no)
        elif (pay_way == '02'):
            #카드결제
            print('card')
            approval_no = today.strftime('%y%m%d') + str(aprv_no)
            CardPay.objects.create(book_no = book_no_qs, approval_no = approval_no)
        else: #포인트결제
            print('point')
            point_history_qs = PointHistory.objects.filter(customer_id__customer_id__exact = customer_id).order_by('usage_date').last()
            rest_point = int(point_history_qs.rest_point)
            point = int(usage_point) * (-1)
            PointHistory.objects.create(customer_id = customer_qs, usage_history = point, rest_point = (rest_point + point))

        #포인트 적립 관련
        if(int(usage_point) == 0):
                point = int(int(pay_money) * 0.1)
                point_history_qs = PointHistory.objects.filter(customer_id__customer_id__exact = customer_id).order_by('usage_date').last()
                rest_point = int(point_history_qs.rest_point)
                PointHistory.objects.create(customer_id = customer_qs, usage_history = point, rest_point = (rest_point + point))
        else:
            print("포인트 사용")

    else:
        print("error")

    data = "done"
    context = { 'data':'complete!' }
    return JsonResponse(context)


def space_append(space, param_string):
    length = len(param_string)
    for i in range(0, space - length):
        param_string = param_string + ' '
    return param_string

def zero_append(space, param_string):
    length = len(param_string)
    for i in range(0, space - length):
        param_string = param_string + '0'
    return param_string


def week2string(weekday):
    if weekday == 0:
        return '월'
    elif weekday == 1:
        return '화'
    elif weekday == 2:
        return '수'
    elif weekday == 3:
        return '목'
    elif weekday == 4:
        return '금'
    elif weekday == 5:
        return '토'
    else:
        return '일'