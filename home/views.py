from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def home(request):
    return HttpResponse("<h4>Hello Sourin</h4>\n<h1>Hello Sourin</h1>")

def success_page(request):
    return HttpResponse("<h1>Server is running.</h1>")

def page(request):
    return render(request, "index.html")

def companies(request):
    companylist = [
        {"name": "Uber", "serial": 100},
        {"name": "Lyft", "serial": 101},
        {"name": "Ola", "serial": 102},
        {"name": "Rapido", "serial": 103},
        {"name": "Didi Chuxing", "serial": 104},
        {"name": "Grab", "serial": 105},
    ]

    for company in companylist:
        print(company)

    return render(request, "index.html", context = {"companylist": companylist})