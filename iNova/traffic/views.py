from django.shortcuts import render

# Create your views here.
def traffic(request):
    return render(request,'websites/traffic.html')
