from django.shortcuts import render, redirect#, reflection
from django.conf.urls import url, include#이거 필요없을듯rom django.http import ttpResponse
from login.models import *
from ticket.models import *
from django.contrib.auth import authenticate, login#try_login에서 사용
from login.my_auth import UserBackend
#from login.models import Customer
#from login.forms import *


#from login.models import Customer
#여기가 실질적인 동작정의(파라미터로 client 요청에 관한 정보가 포함된
#request객체를 받으며최종적으로 request객체를 만들어서 반환해야한다.)
#respoinse객체는 직접 생성할 수도 있고, template renderer를 호출하여
#응답할 markup이 포함된 response객체를 반환받을 수도 있다.
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView # 오브젝트를 생성하는 뷰 (form 혹은 model과 연결되서 새로운 데이터를 넣을 때 CreateView - generic view를 사용)
# Create your views here.

from django.http import HttpResponse
#from fernet_fields import EncryptedCharField, EncryptedTextField


#from .models import Customers#이 table도 화면에 보여지게 쓰겠다###################

# Create your views here.
#def login_request(request):
#    msg = 'login view My Message'
#    return render(request, 'login\login_request.html',{'message':msg}) #index위치에 의미있는거 들어가야하나?
#def login_page(request):
#    #return HttpResponse("Hello, World!")
#    msg = 'login view My Message'
#    return render(request, 'login\login_page.html',{'message':msg}) #index위치에 의미있는거 들어가야하나?

#def make_account(request, account):#이거 회원가입 만들어사 연결해야할거
#    return HttpResponse(acocunt)#???이거 틀린듯 account라 적은곳에 회원가입창에서 띄울거 보여줘야한다

#로그인페이지로 들어오는건 내가하는부분에서는 아닌듯 연결할때

#def temp_index(request):#이거 index말고 다른이름도 괜찮나? 아닌듯 login안에 있는 index.html인듯
    #return HttpResponse("Hello, World!")
#    msg = 'login view My Message'
#    customers = Customer.objects.all()#앞의 customers 변수는 Customer table의 모든 행(object)들을 불러와 DB에 가지게 된다 뒤의 Customer는 DB의 table이름이다


#    str = ''#빈 string변수생성
#    for customer in customers:
#        str += "{} :아이디 {} :이름 ({}) :비밀번호".format(customer.customer_id, customer.customer_name, customer.pwd)
#        str += customer.member_check+"<p>"#"안의 부분은 html이다"
#    return HttpResponse(str)
#    return render(request, 'login\index.html')#,{'message':msg})#여기 index.html의 내용을 보여주도록 적음

#   return HttpResponse("Hello world") 페이지 열어달라는 요청에 hello world라는 string보여줌
#request종류 어떻게 구분????



#########회원가입

#def index(request):#디비에서 정보 받아오기, 회원정보조회할때수정해서사용


#    return render(request, 'login/make_account_index', context)
#    str = ''
#    for customer in customer_list:#Customer table가지고 있는 customer 변수를 하나씩 받아옴?
#        str += "<p>{} :아이디 {} :이름 ({}) :비밀번호<br>".format(customer.customer_id, customer.customer_name, customer.pwd)
#        str += customer.member_check+"</p>"#"안의 부분은 html이다"
#    return HttpResponse(str)

#def make_accounts(request, customer_id, customer_name, rrn, contact, pwd, member_check, email):
#    customer_list = Customer.objects.all()#디비에서 Customer table 의 내용 받아옴
#    context = {'customers':customer_list}#앞의 customers맞나? 정의하는 변수이름인가?
#
#    try:
#        #new_account = request.POST['customer_id, customer_name, rrn, contact, pwd, member_check, email']
#        new_account = Customer(customer_id=Customer.customer_id, customer_name=Customer.customer_name, rrn=Customer.rrn, contact=Customer.contact, pwd=Customer.pwd, member_check=Customer.member_check, email=Customer.email)
#        new_account.save()
#    except:
#        customer_id=NULL
#
#    return httpResponse("회원가입되었습니다!")#이거 로그인된 홈페이지로 보내도록바꾸기
#
#def test_data_insert(request):
#    #화면에서 data받아오기
#
#    #받아온 data customer_object객체게 저장하기
#    customer_object = Customer(customer_id=Customer.customer_id, customer_name=Customer.customer_name, rrn=Customer.rrn, contact=Customer.contact, pwd=Customer.pwd, member_check=Customer.member_check, email=Customer.email)
#    #Customer는 table이름이다
#
#    #새 객체 INSERT
#    customer_object.save
#def show_login_index(request):#, area):
#    return render(request, 'login/index.html')

#def make_account_index(request):#, area):
#    return render(request, 'login\make_account.html')
#    #return HttpResponse("Hello world")

def nonmember_temp_account(request):
    customer_list = Customer.objects.all()#디비에서 Customer table 의 내용 받아옴
    return render(request, 'login/nonmember_temp_account.html')
def made_nonmember_account(request):
    if request.method =='POST':
        customer_id = request.POST['n_id']
        #customer_id = request.POST.get('customer_id')
        customer_name = request.POST['n_name']
        dob = request.POST['n_birth']
        contact = request.POST['n_tel']
        email = request.POST['n_email']
        member_check ='N'# request.POST['m_member_check']

        pwd = request.POST['n_pass']#이거 데이터 타입 패스워드전용으로 비교할수 있는거 있는지 찾아보기
        #vaults = Vault.objects.filter(customer_id=customer_id).filter(Type='1account')#customer_id 말고 pwd로 해야할수도있고 뒤의 필터도 없애보기
        #vaults = Vault.objects.filter(User=request.user).filter(Type='1account')


        new_customer=Customer.objects.create(customer_id=customer_id, customer_name=customer_name, dob=dob, contact=contact, pwd=pwd, member_check=member_check, email=email)

        new_customer.save()
        return redirect('../login')


def make_accounts(request):
    customer_list = Customer.objects.all()#디비에서 Customer table 의 내용 받아옴
    return render(request, 'login/make_account.html')
def made_new_account(request):
    if request.method =='POST':
        customer_id = request.POST['m_id']
        #customer_id = request.POST.get('customer_id')
        customer_name = request.POST['m_name']
        dob = request.POST['m_birth']
        contact = request.POST['m_tel']
        email = request.POST['m_email']
        member_check = 'Y'#request.POST['m_member_check']

        pwd = request.POST['m_pass']#이거 데이터 타입 패스워드전용으로 비교할수 있는거 있는지 찾아보기
        #vaults = Vault.objects.filter(customer_id=customer_id).filter(Type='1account')#customer_id 말고 pwd로 해야할수도있고 뒤의 필터도 없애보기
        #vaults = Vault.objects.filter(User=request.user).filter(Type='1account')


        new_customer=Customer.objects.create(customer_id=customer_id, customer_name=customer_name, dob=dob, contact=contact, pwd=pwd, member_check=member_check, email=email)
        new_customer.save()
        new_customer_point = PointHistory.objects.create(customer_id = customer_id, usage_point = 500, rest_point = 500)

        return redirect('../login')
    #    return redirect('/login/')

#username = request.session['customer_id']
#customers = Customer.objects.filter(customer_id=username)
#context = {'customers':customers}
#return render(request, 'login/mypage.html', context)



#def made_new_account(request):#회원가입시 두개의 디비에 각 저장되도록
#    if request.method =='POST':
#        customer_id = request.POST['m_id']
#        customer_name = request.POST['m_name']
#        dob = request.POST['m_birth']
#        contact = request.POST['m_tel']
#        pwd = request.POST['m_pass']#이거 데이터 타입 패스워드전용으로 비교할수 있는거 있는지 찾아보기
#        email = request.POST['m_email']
#        member_check = request.POST['m_member_check']
#        new_user=User.objects.create(username=customer_id, password=pwd)#이거 잘 입력한건가?
#        new_user.customer.customer_name = custmomer_name
#        new_user.customer.dob = dob
#        new_user.customer.contact = contact
#        new_user.customer.email = email
#        new_user.customer.member_check = member_check
        #User table의 username에 customer id들어간다
#        new_user.save()

        #new_customer=Customer.objects.create(customer_id=User.username, customer_name=customer_name, dob=dob, contact=contact, pwd=pwd, member_check=member_check, email=email)
        #new_customer.save()
#        return redirect('../')


def try_login(request):
    #msg = 'login view My Message'
    #customers = Customer.objects.all()#앞의 customers 변수는 Customer table의 모든 행(object)들을 불러와 DB에 가지게 된다 뒤의 Customer는 DB의 table이름이다
    #customers 변수에 table내용 다 받아옴

    if request.method =='POST':
        username = request.POST['m_id']
        password = request.POST['m_pass']
    user = UserBackend.authenticate(request, customer_id=username, pwd=password) # 직접 만든 custom 인증으로 회원이 맞는지 확인
    #장고의 기본인증은 usermodel을 default로 가지고 있기 때문에 customer에는 적용이 안되므로 직접 만들었음

    if user is not None:
        request.session['customer_id'] = username # 인증을 거치고 난 user의 세션 생성
#        customers = Customer.objects.filter(customer_id=username)
#        context = {'customers':customers}
        return redirect('../')
    else:
        return HttpResponse("아이디나 비밀번호가 일치하지 않습니다.")

#def mypage(request):

#    return render(request, 'login\mypage.html')

def mypage(request):
    #customers = Customer.objects.all()
    #context = {'customers':customers}
    #context = {'customer_id':customer_id, 'customer_name':customer_name, 'dob':dob, 'contact':contact, 'pwd':pwd, 'member_check':member_check, 'email':email}

    if request.session['customer_id']:
        username = request.session['customer_id']
        customers = Customer.objects.filter(customer_id=username)
        context = {'customers':customers}
        return render(request, 'login/mypage.html', context)

def my_info(request):#주소에 mypage넣어야할수도
    if request.session['customer_id']:
        username = request.session['customer_id']
        customers = Customer.objects.filter(customer_id=username)
        context = {'customers':customers}
        return render(request, 'login/my_info.html', context)

def check_reservation(request):
    if request.session['customer_id']:
        username = request.session['customer_id']#username은 컬럼의값하나
        pays = Pay.objects.filter(customer_id=username)#pays는 객제?
        book_no = pays.values("book_no")
        ticket_infos = TicketInfo.objects.filter(book_no=book_no)
        ticket_no = ticket_infos.values("ticket_no")

        tickets = Ticket.objects.filter(ticket_no=ticket_no)
        scrn_schd_no = tickets.values("scrn_schd_no")
        scrn_schds = ScrnSchd.objects.filter(scrn_schd_no=scrn_schd_no)

        context = {'scrn_schds':scrn_schds}
        #str2 = scrn_schds
        #return HttpResponse(str2)
        return render(request, 'login/check_reservation.html', context)

def my_point(request):
    if request.session['customer_id']:
        username = request.session['customer_id']
        points = PointHistory.objects.filter(customer_id=username)
        context = {'points':points}
        return render(request, 'login/my_point.html', context)

def nonlogin_check_reservation(request):#이거 지우기
    customer_list = Customer.objects.all()
    #HttpResponse("수정중")
    return render(request, 'login/nonlogin_check_reservation.html')

def check_with_id(request):
    if request.session['customer_id']:
        username = request.session['customer_id']
        customers = Customer.objects.filter(customer_id=username)


        context = {'customers':customers}
        return render(request, 'login/mypoint.html', context)
def check_with_phonenumber(request):
    if request.session['customer_id']:
        username = request.session['customer_id']
        customers = Customer.objects.filter(customer_id=username)



        context = {'customers':customers}
        return render(request, 'login/mypoint.html', context)

    #for customer in customers:
        #if user.username == customer.customer_id :
            #if user.password == customer.pwd :
            #    return redirect('../')
            #else :
                #return HttpResponse("비밀번호가 불일치")

    #return HttpResponse("존재하지않는 아이디입니다.")
def logout(request):
    request.session.flush() # 세션 비우기
    return redirect('../')

#    str = ''#빈 string변수생성
#    for customer in customers:
#        str += "{} :아이디 {} :이름 ({}) :비밀번호".format(customer.customer_id, customer.customer_name, customer.pwd)
#        str += customer.member_check+"<p>"#"안의 부분은 html이다"
#    return HttpResponse(str)

#    customer_list = Customer.objects.all()#디비에서 Customer table 의 내용 받아옴
#    return render(request, 'login/temp.html', {'customer_list' : customer_list}

#    )

#    def check_if_user(user_id, uer_pw){
#        payload = {

#        }
#    }
#def user_mode(request):#수정중
#    customer_list = Customer.objects.all()#디비에서 가져온내

#    user_input = {#화면에서 입력받은 값
#        'user_id' : str(user_id),
#        'user_pw' : str(user_pw)
#    }
#디비내용이랑 화면에서 입력받은값 비교하는 함수 구현
        #Customer.objects.create(customer_id=customer_id, customer_name=customer_name, dob=dob, contact=contact, pwd=pwd, member_check=member_check, email=email)
#        return redirect('../')
    #    return redirect('/login/')

    #디비에서 Customer table 의 내용 받아옴
#    return render(request, 'login/temp.html', {'customer_list' : customer_list}#?
#    )
#def test_data_insert(request):
    #화면에서 data받아오기

    #받아온 data customer_object객체게 저장하기
#    customer_object = Customer(customer_id=Customer.customer_id, customer_name=Customer.customer_name, rrn=Customer.rrn, contact=Customer.contact, pwd=Customer.pwd, member_check=Customer.member_check, email=Customer.email)
#Customer는 table이름이다

    #새 객체 INSERT
#    customer_object.save



#def create(request):
#    if request.method=='POST': #저장버튼을 눌러서 HTTP POST가 전달될때
#        form = login_form(request.POST)# 사용자 정의form 인 login_form() 생성자의 파라미터로
#        if form.is_valid():
#            form.save()
#        return redirect('/login/list')##이거 주소 바꿔야할것같은데??
#    else:
#        form = login_form()#login_form는 Customer tale의 내용의 data를 전달하도록 하는 form
#
#    return render(request, 'feedback.html', {'form': form})##