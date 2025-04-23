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
from PIL import Image
import torch
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
    return render(request, 'Traffic_page/footage_1.html')

def detect_vehicles(image_path):
    # Load YOLO model (ensure you have YOLOv5 installed and the model is loaded correctly)
    
    model  = YOLO(r'anomaly/MLModels/best.pt') # Load the YOLO model (small version for speed)
    
    # Load image
    img = Image.open(image_path)

    # Inference
    results = model(img)

    # Get the count of detected vehicles (you can filter based on 'car', 'bus', 'truck', etc.)
    vehicle_count = len([x for x in results.xywh[0] if x[5] in [0, 1, 3, 6]])  # Filter for vehicle classes
    return vehicle_count

# Function to handle the upload and processing of images
def process_images(request):
    if request.method == 'POST' and request.FILES.getlist('image1'):
        fs = FileSystemStorage()
        vehicle_counts = []

        # Loop through the 4 images
        for i in range(1, 5):
            uploaded_file = request.FILES.get(f'image{i}')
            if uploaded_file:
                # Save the uploaded file
                file_path = fs.save(uploaded_file.name, uploaded_file)
                file_url = fs.url(file_path)
                
                # Run YOLO model on the uploaded image
                vehicle_count = detect_vehicles(f'media/{file_path}')
                vehicle_counts.append(vehicle_count)

        # Return the results as JSON
        print('vehicle_counts:', vehicle_counts)
        return JsonResponse({'vehicle_counts': vehicle_counts})

    # return render(request, 'Trafic_page/footage_1.html')



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
    


