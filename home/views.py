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

    # for company in companylist:
    #     print(company)

    text = """Lorem ipsum dolor sit amet consectetur adipisicing elit. Quia debitis error cupiditate corporis adipisci suscipit odit, officia est quam veritatis asperiores eos laboriosam, possimus molestiae laborum? Perferendis sunt consequatur dicta ut excepturi magni quod voluptates pariatur repellat delectus architecto exercitationem enim esse, eum, veritatis tempora, quae voluptate eos dolores iure impedit asperiores dolorem. Tempora officiis voluptatibus quis fugit odio facilis architecto molestiae quas minus, dolorum ad vitae hic sunt quo corporis ab nobis odit amet magnam, porro quaerat numquam corrupti. Officiis, illum? Ipsum odio veritatis ipsa quas inventore, iste mollitia aut, eaque, deserunt eum id expedita delectus? Obcaecati, earum praesentium."""
    vegetables = ["Pumpkin", "Tomato", "Potatoe"]

    return render(request, "index.html", context={"companylist": companylist, "text": text, "vegetables": vegetables, "pagename": "Index"})

def about(request):
    return render(request, "about.html", context={"pagename": "About"})

def contact(request):
    return render(request, "contact.html", context={"pagename": "Contact"})