from django.shortcuts import render

def index(request):
    #return HttpResponse("Hello, World!")
    msg = 'Main Index Page'
    return render(request, 'index.html',{'message':msg})