from django.shortcuts import render

###추가
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    #return HttpResponse("Hello, World!")
    msg = 'My Message'
    return render(request, 'test_app\index.html',{'message':msg})

# def index2(request):
#     #return HttpResponse("Hello, World!")
#     msg = 'movie111111111 view My Message'
#     return render(request, 'movie\index2.html',{'message':msg})
