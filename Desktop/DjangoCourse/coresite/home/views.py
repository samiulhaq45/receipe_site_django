from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    peoples = [
        {"name": "Sami Ul Haq", "age":23},
        {"name": "Kashif Aziz", "age":22},
        {"name": "Danish Ali", "age":21},
        {"name": "Daniyal Khan", "age":17},
        {"name": "Shoaib Ahmed", "age":24},
        {"name": "Yasir Khan", "age":20},
        {"name": "Awais Ali", "age":15},
    ]
    return render(request, 'index.html', context={"peoples": peoples})

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")
    