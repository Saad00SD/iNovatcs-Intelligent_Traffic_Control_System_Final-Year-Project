from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    members  = [
        {"name": "Saad", "role": "Project Lead","image":"images/members/member1.jpg"},
        {"name": "Dhilham","role":"Front-End Developer","image":"images/members/member2.jpg"},
        {"name": "Rikhaz","role":"Front-End Developer","image":"images/members/member3.jpg"},

    ]
    return render(request,'websites/home.html',{"members":members})


def about(request):
    return HttpResponse("Message from about")


