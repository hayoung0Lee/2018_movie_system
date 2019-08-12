from django.shortcuts import render
# Create your views here.
###추가
from django.http import HttpResponse
from .forms import PostForm, DeleteForm, SchdSearchForm, MovieSchdForm
from django.db.models import Q
from .models import Seat, Theater
from django.shortcuts import redirect, render
from .models import Movie, ScrnClass
from ticket.models import ScrnSchd, Ticket
import datetime
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.views.decorators.http import require_POST
from django.core import serializers
from django.db import connection

# Create your views here.
def index(request):
    today = datetime.date.today()
    movies = Movie.objects.filter(scrn_date__lt=today)
    
    for movie in movies:
        movie.scrn_date = movie.scrn_date.strftime('%Y.%m.%d')
    
    context = { 'movies':movies }
    return render(request, 'movie_index.html', context)

def movie_yet(request):
    today = datetime.date.today()
    d_day_list = []
    movies = Movie.objects.filter(scrn_date__gt=today)
    for movie in movies:
        d_day = movie.scrn_date.day - today.day
        movie.scrn_date = movie.scrn_date.strftime('%Y.%m.%d')
        movie.d_day = d_day
    context = { 'movies':movies }
    return render(request, 'movie_yet.html', context)

def movie_detail(request, pram_movie_no):
    movie = Movie.objects.get(movie_no = pram_movie_no)
    movie.scrn_date = movie.scrn_date.strftime('%Y.%m.%d')
    context = { 'movie':movie }
    return render(request, 'movie_detail.html', context)

    msg = 'movie view My Message'
    return render(request, 'movie/index.html',{'message':msg})


def seat_check(request):
    return redirect(post_detail)
    #return render(request, 'movie/seat_check.html')



def post_detail(request):
    instance = Seat.objects.values_list('theater_no',flat=True)
    #now_on_list = list(set(instance))

    arr =[]
    for i in instance:
        arr.append(i.strip())
    now_on_list = list(set(arr))


    return render(request, 'movie/post_detail.html',{'msg':now_on_list})

    #현재 좌석 테이블에 있는 키들을 다 가지고 와서 상영관 정보만 보여주기
    #instance = Seat.objects.all()
    #now_on_list = list(set(instance))

def post_show(request, pk):
    #좌석 옵션
    seat_in = Seat.objects.filter(theater_no = pk)

    list = []
    for i in seat_in:
        print(i.seat_no)
        #list.append(i.seat_no.replace(' &#39',''))
        list.append(i.seat_no)

    list = json.dumps(list)

    return render(request, 'movie/post_show.html', {'list': list})




def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            theater = form.cleaned_data.get('theater_no')
            picked_A = form.cleaned_data.get('name_A')
            picked_B = form.cleaned_data.get('name_B')
            picked_C = form.cleaned_data.get('name_C')
            picked_D = form.cleaned_data.get('name_D')
            picked_E = form.cleaned_data.get('name_E')
            picked_F = form.cleaned_data.get('name_F')
            picked_G = form.cleaned_data.get('name_G')

            for a in picked_A:
                 p = Seat(theater_no=theater,seat_no=a)
                 p.save()

            for b in picked_B:
                 p = Seat(theater_no=theater,seat_no=b)
                 p.save()

            for c in picked_C:
                 p = Seat(theater_no=theater,seat_no=c)
                 p.save()

            for d in picked_D:
                 p = Seat(theater_no=theater,seat_no=d)
                 p.save()

            for e in picked_E:
                 p = Seat(theater_no=theater,seat_no=e)
                 p.save()

            for f in picked_F:
                 p = Seat(theater_no=theater,seat_no=f)
                 p.save()

            for g in picked_G:
                 p = Seat(theater_no=theater,seat_no=g)
                 p.save()



            return redirect('post_detail')

            #rqs = Theater.objects.raw('Select theater_no from Theater where theater_name = %s',[theater])
            #tuples = tuple((o.theater_no) for o in rqs)

            # for p in rqs:
            #     print(p)
            # do something with your results


    else:
        form = PostForm()

    return render(request, 'movie/post_edit.html', {'form': form})


def post_delete(request):
    if request.method == "POST":
        form = DeleteForm(request.POST)
        if form.is_valid():
            theater = form.cleaned_data.get('theater_no')
            #rqs = Theater.objects.raw('Select theater_no from Theater where theater_name = %s',[theater])
            #tuples = tuple((o.theater_no) for o in rqs)

            #print(Ticket.objects.filter(theater_no=).count())

            print(Ticket.objects.filter(theater_no=theater.theater_no[0:2]).count())

            if(Ticket.objects.filter(theater_no=theater.theater_no[0:2]).count() > 0):
                return render(request,'movie/error.html')
            else:
                Seat.objects.filter(theater_no=theater).delete()

            # for p in rqs:
            #     print(p)
            # # do something with your results
            return redirect('post_detail')
    else:

        instance = Seat.objects.values_list('theater_no',flat=True)
        now_on_list = list(set(instance))
        # rows = Seat.objects.distinct('theater_no')
        form = DeleteForm()

    return render(request, 'movie/post_delete.html', {'form': form, 'now':now_on_list})


def movie_now(request):
    return render(request, 'movie/movie_now.html')




def movie_schd_daily(request):
    #year = request.GET['year']
    #print(year)
    time = ['06:00:00', '06:30:00','07:00:00','07:30:00','08:00:00', '08:30:00', '09:00:00', '09:30:00','10:00:00','10:30:00','11:00:00','11:30:00','12:00:00','12:30:00','13:00:00']
    time += ['13:30:00', '14:00:00','14:30:00','15:00:00','15:30:00','16:00:00','16:30:00','17:00:00','17:30:00','18:00:00','18:30:00','19:00:00','19:30:00','20:00:00','20:30:00', '21:00:00', '21:30:00']
    time += ['22:00:00','22:30:00','23:00:00','23:30:00','00:00:00','00:30:00','01:00:00','01:30:00','02:00:00','02:30:00' ]
    if request.method == "POST":
        form = MovieSchdForm(request.POST)
        if form.is_valid():
            #상영일정 등록
            scrn_schd_no = ScrnSchd.objects.all().count() + 1
            scrn_date = request.POST['scrn_date']
            movie_selected = form.cleaned_data.get('Movies').values_list('movie_no')
            theater_selected = form.cleaned_data.get('Theaters')
            scrn_ep = request.POST['scrn_ep']
            start_time = request.POST['start_options']
            end_time =  request.POST['end_options']


            #상영일정 등록
            new_schd = ScrnSchd(
                scrn_schd_no=scrn_schd_no,
                theater_no=Theater.objects.get(theater_no=theater_selected[0]),
                scrn_date=scrn_date,
                scrn_ep=scrn_ep,
                start_time=start_time,
                end_time=end_time,
                movie_no=Movie.objects.get(movie_no=movie_selected),
                )
            print("11",new_schd)
            new_schd.save()

            #티켓 테이블 생성
            ticket_no = Ticket.objects.all().count() + 1
            thea_num = Theater.objects.get(theater_no=theater_selected[0])
            seat_all = Seat.objects.filter(theater_no= theater_selected[0])

            cursor = connection.cursor()
            # cursor.execute("INSERT INTO TICKET (ticket_no, book_avail_check, seat_no, theater_no, scrn_schd_no) VALUES({}, {},{},{},{})".format(str(ticket_no), '0', 'A1', thea_num.theater_no[0:2] , str(scrn_schd_no)))

            #cursor.execute("INSERT INTO TICKET (ticket_no, book_avail_check, seat_no,theater_no, scrn_schd_no) VALUES('1','0','A1','01','3');")
            #cursor.execute("INSERT INTO TICKET (ticket_no, book_avail_check, seat_no,theater_no, scrn_schd_no) VALUES (%s, %s, %s,%s,%s);",('1','0','A1','01','3'))

            #(%s, %s, %s)", (var1, var2, var3)

            for i in seat_all:
                ticket_no_temp = zero_append(6, str(ticket_no))
                #print("INSERT INTO TICKET (ticket_no, book_avail_check, seat_no,theater_no, scrn_schd_no) VALUES (%s, %s, %s,%s,%s);",(str(ticket_no),'0',i.seat_no.replace(" ",""),thea_num.theater_no[0:2],str(scrn_schd_no)))
                #cursor.execute("INSERT INTO TICKET (ticket_no, book_avail_check, seat_no,theater_no, scrn_schd_no) VALUES (%s, %s, %s,%s,%s);",(str(ticket_no),'0',i.seat_no.replace(" ",""),thea_num.theater_no[0:2],str(scrn_schd_no)))
                seat_temp = seat_append(3, str(i.seat_no.replace(" ","")))
                theater_temp = thea_num.theater_no[0:2]
                t_temp = theater_temp + ticket_no_temp + seat_temp
                print(t_temp)
                cursor.execute("INSERT INTO TICKET (ticket_no, book_avail_check, seat_no,theater_no, scrn_schd_no) VALUES (%s, %s, %s,%s,%s);",(t_temp,'0',i.seat_no.replace(" ",""),thea_num.theater_no[0:2],str(scrn_schd_no)))
                
                ticket_no = ticket_no + 1
                #sentence = "INSERT INTO TICKET VALUES({},{},{},{},{});".format(str(ticket_no),'0',i.seat_no.replace(" ",""),thea_num.theater_no[0:2],str(scrn_schd_no))
                #print(sentence)
                #cursor.execute("INSERT INTO TICKET VALUES('1','0','A1','01','3');")
                #print(sentence)
                #cursor.execute(sentence)
            # cursor.commit()
            cursor.close()


            # ticket_no = Ticket.objects.all().count() + 1
            #
            # seat_all = Seat.objects.filter(theater_no= theater_selected)
            # print("22",seat_all)
            #
            # #rqs = Theater.objects.raw('Select theater_no from Theater where theater_name = %s',[theater])
            # #tuples = tuple((o.theater_no) for o in rqs)
            #
            # # for p in rqs:
            # #     print(p)
            # # do something with your results
            # thea_num = Theater.objects.get(theater_no=theater_selected)
            #
            # print(thea_num.theater_no)
            #
            #
            # #rqs = Ticket.objects.raw('INSERT INTO TICKET VALUES(%s, %s,%s,%s,%s)',[ticket_no, 0, 'A1', thea_num.theater_no[0:2] , scrn_schd_no])
            #
            # for i in seat_all:
            #     print([ticket_no, 0, i.seat_no, thea_num.theater_no[0:2],scrn_schd_no])
            #     rqs = Ticket.objects.raw('INSERT INTO TICKET VALUES(%s, %s,%s,%s,%s)'%(ticket_no, 0, i.seat_no, thea_num.theater_no[0:2] , scrn_schd_no))
            #
            #     ticket_no = ticket_no + 1

            #티켓 테이블 생성
            return render(request,'movie/movie_schd.html')

            #rqs = Theater.objects.raw('Select theater_no from Theater where theater_name = %s',[theater])
            #tuples = tuple((o.theater_no) for o in rqs)

            # for p in rqs:
            #     print(p)
            # do something with your results
    else:
        form = MovieSchdForm()

    return render(request, 'movie/movie_schd_daily.html',{'form': form,'time':time})


def zero_append(zeros, param_string):
    length = len(param_string)
    zero_string = '0' * (zeros - length)
    temp = zero_string + param_string
    return temp

def seat_append(zeros, param_string):
    length = zeros - len(param_string)
    if (length > 0):
        temp = param_string[0] + param_string
    else:
        temp = param_string
    return temp


#ajax용으로 추가된 뷰들
def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': Movie.objects.filter(movie_name__iexact=username).exists()
    }
    return JsonResponse(data)

#날짜별 상영일정을 반환해주는 뷰(ajax용)

@csrf_exempt
def search_schd(request):
    print('1')
    if request.method == 'POST':
        print('2')
        search_date = request.POST.get('date', None)
        print(search_date)

        #all = ScrnSchd.objects.filter(scrn_date__iexact = search_date)
        #all = ScrnSchd.objects.all()
        #data_all = serializers.serialize('json', ScrnSchd.objects.all())

        time = ['06:00:00', '06:30:00','07:00:00','07:30:00','08:00:00', '08:30:00', '09:00:00', '09:30:00','10:00:00','10:30:00','11:00:00','11:30:00','12:00:00','12:30:00','13:00:00']
        time += ['13:30:00', '14:00:00','14:30:00','15:00:00','15:30:00','16:00:00','16:30:00','17:00:00','17:30:00','18:00:00','18:30:00','19:00:00','19:30:00','20:00:00','20:30:00', '21:00:00', '21:30:00']
        time += ['22:00:00','22:30:00','23:00:00','23:30:00','00:00:00','00:30:00','01:00:00','01:30:00','02:00:00','02:30:00' ]


        #조인한 결과
        rqs = ScrnSchd.objects.raw('select * from theater, scrn_schd where theater.theater_no = scrn_schd.theater_no and scrn_date = %s',[search_date])

        #이렇게 안읽으면 오류남
        #lists = list([o.theater_name, o.scrn_date, o.start_time, o.end_time] for o in rqs)
        lists = []
        for o in rqs:
            lists.append([o.theater_name, o.scrn_date, o.start_time, o.end_time, time.index(o.start_time.strftime('%H:%M:00'))+1, time.index(o.end_time.strftime('%H:%M:00'))+1])


        #리스트들을 json형식으로 바꿀수 있게 준비하는 과정
        print(lists)
        data = {}
        i = 0
        for d in lists:
            data[i] = d
            i = i+1
        #json데이터를 읽기 좋도록 길이를 추가
        data['size'] = len(data)

        #우리한테 있는 상영관수를 읽어와야함.
        Theater_info = Theater.objects.all()
        data['theater_count'] = Theater_info.count()

        count = 0
        for i in Theater_info:
            data['theater' + str(count)] = i.theater_name
            count = count+1

        data['time'] = time
        # 참고했던 코드들 아직 둬야함,,, 어떻게 될지 몰라서...
        # data_all = serializers.serialize('json', rqs)
        # data_all = json.loads(data_all)
        # print("ddd")
        # print(data_all)
        # #길기 읽어오기
        # size = ScrnSchd.objects.filter(scrn_date=search_date).count()
        # lists = list([o.theater_no, o.theater_name, o.scrn_date] for o in rqs)
        #
        # #len = len(lists)
        #
        # #json형식으로 수정
        # data = {}
        # data['size'] = size
        #
        # i = 0
        # for d in data_all:
        #     data[i] = d
        #     i = i+1
        #
        # print(data)



        #lists = list(tuples)

        #
        # print(lists)
        # #
        # # #필터링
        # all = ScrnSchd.objects.filter(scrn_date=search_date)
        # #size
        # size = all.count()
        #
        #
        # data_all = serializers.serialize('json', all)
        # data_all = json.loads(data_all)
        #
        #
        #
        #
        #
        # data = {
        #     'size': size,
        #     'list': data_all,
        # }
        #
        # print(data)
    return JsonResponse(data)

    #return HttpResponse(json.dumps(all), content_type='application/json')
    #return HttpResponse(json.dumps(dict), content_type='application/json')