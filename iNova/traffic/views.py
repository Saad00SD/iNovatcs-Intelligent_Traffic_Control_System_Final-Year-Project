from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def footage_1(request):
    return render(request, 'Traffic_page/footage_1.html')

def footage_2(request):
    return render(request, 'Traffic_page/footage_2.html')

def footage_3(request):
    return render(request, 'Traffic_page/footage_3.html')

def footage_4(request):
    return render(request, 'Traffic_page/footage_4.html')

def traffic(request):
    return render(request, 'websites/traffic.html')

import cv2
import numpy as np
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .forms import VideoUploadForm
from ultralytics import YOLO
import tempfile
import os

model  = YOLO(r'anomaly/MLModels/best.pt')

def footage_1(request):
    context = {}
    if request.method == 'POST' and request.FILES['video_file_1']:
        video_file = request.FILES['video_file_1']
        fs = FileSystemStorage()
        filename = fs.save(video_file.name, video_file)
        video_url = fs.url(filename)

        # Process the video to count vehicles and display traffic light
        vehicle_counts, traffic_lights = process_video(fs.url(filename))

        context['video_url'] = video_url
        context['vehicle_counts'] = vehicle_counts
        context['traffic_lights'] = traffic_lights

    form = VideoUploadForm()
    context['form'] = form
    return render(request, 'Traffic_page/footage_1.html', context)

    
def process_video(video_path):
    # Open the video file
    cap = cv2.VideoCapture(video_path)
    
    vehicle_counts = []
    traffic_lights = []
    
    while cap.isOpened():
        ret, frame = cap.read()
        print("video process:", ret)
        if not ret:
            break
        
        # Use YOLO model to detect vehicles
        results = model(frame)

        # Debugging: Check the results (this will print detected vehicles in the frame)
        print("Detection results:", results.pandas().xywh)

        # Count the vehicles detected
        vehicle_count = len(results.pandas().xywh)  # Assuming pandas() returns the detection data
        
        vehicle_counts.append(vehicle_count)

        # Based on the vehicle count, determine the traffic light color
        if vehicle_count < 5:
            traffic_lights.append("green")
        elif vehicle_count < 15:
            traffic_lights.append("yellow")
        else:
            traffic_lights.append("red")
        
        # Draw the traffic light on the frame (optional)
        cv2.putText(frame, f"Traffic Light: {traffic_lights[-1]}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Show the frame with traffic light (for debugging, can be removed later)
        cv2.imshow('Frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Release the video capture
    cap.release()
    cv2.destroyAllWindows()
    
    return vehicle_counts, traffic_lights
    


# Assuming you have a method to process the image (e.g., YOLO model)
@csrf_exempt
def detect_vehicles(request):
    # Extract image ID or image file from the request
    image_id = request.POST.get('image_id')

    # Use your vehicle detection model here to process the image and get the vehicle count
    vehicle_count = 10  # This is just a placeholder for demonstration

    return JsonResponse({'vehicle_count': vehicle_count})


