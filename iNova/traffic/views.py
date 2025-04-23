from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import cv2
import numpy as np
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .forms import VideoUploadForm
from ultralytics import YOLO
import tempfile
import os
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse



# def footage_1(request):
#     return render(request, 'Traffic_page/footage_1.html')

@login_required
def footage_2(request):
    return render(request, 'Traffic_page/footage_2.html')

@login_required
def footage_3(request):
    return render(request, 'Traffic_page/footage_3.html')

@login_required
def footage_4(request):
    return render(request, 'Traffic_page/footage_4.html')

@login_required
def traffic(request):
    return render(request, 'websites/traffic.html')

def upload_images(request):
    if request.method == 'POST' and request.FILES.getlist('images'):
        fs = FileSystemStorage()
        # Loop over the list of images uploaded
        for uploaded_file in request.FILES.getlist('images'):
            # Save each uploaded file with a unique name
            fs.save(uploaded_file.name, uploaded_file)
    return render(request, 'footage_1.html')


model  = YOLO(r'anomaly/MLModels/best.pt')

@login_required
def footage_1(request):
    return render(request, 'Traffic_page/footage_1.html',)


def vehicle_count(request):
    result = model.predict()


def process_video(video_path):

    cap = cv2.VideoCapture(video_path)
    
    vehicle_counts = []
    
    while cap.isOpened():
        ret, frame = cap.read()
        print("video process:", ret)
        if not ret:
            break
        
        # Use YOLO model to detect vehicles
        results = model(frame)

        # # Debugging: Check the results (this will print detected vehicles in the frame)
        # print("Detection results:", results.pandas().xywh)

        # Count the vehicles detected
        vehicle_count = len(results.pandas().xywh)  # Assuming pandas() returns the detection data
        
        vehicle_counts.append(vehicle_count)

    
    return vehicle_counts
    


