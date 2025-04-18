from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os
from ultralytics import YOLO
import time
model  = YOLO(r'anomaly/MLModels/best.pt')

def footage_1(request):
    return render(request, 'Traffic_page/footage_1.html')

def footage_2(request):
    return render(request, 'Traffic_page/footage_2.html')

def footage_3(request):
    return render(request, 'Traffic_page/footage_3.html')

def footage_4(request):
    return render(request, 'Traffic_page/footage_4.html')

from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os


def traffic(request):
    
    return render(request, 'Traffic_page/footage_1.html')
