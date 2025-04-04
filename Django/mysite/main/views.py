from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    data = {
        'title': 'Поступление',
        'values': ['Play', 'game', 'over']
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')

def wheather(request):  
    return render(request, 'main/wheather.html')

def page_itwo(request):  
    return render(request, 'main/index2.html')

def page_atwo(request):  
    return render(request, 'main/about2.html')

def page_wtwo(request):  
    return render(request, 'main/wheather2.html')