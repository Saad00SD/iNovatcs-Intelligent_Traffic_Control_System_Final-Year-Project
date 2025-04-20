from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from .yolo_fire import run_fire_detection
from ultralytics import YOLO
from django.shortcuts import render
from django.http import StreamingHttpResponse
from django.conf import settings
from .forms import VideoUploadForm
import os, uuid, cv2
from django.contrib.auth.decorators import login_required
from .models import TrafficData
from .forms import IncidentReportForm
from django.http import JsonResponse






uploaded_video_path = None  # global var for streaming
is_fire  = False
is_smoke = False
is_accident = False



model  = YOLO(r'anomaly/MLModels/best.pt')
model2 = YOLO(r'anomaly/MLModels/best_both.pt')


# Views for each footage
def foot_1(request):
    return render(request, 'Anomaly_pages/footage_1.html')

def foot_2(request):
    return render(request, 'Anomaly_pages/footage_2.html')

def foot_3(request):
    return render(request, 'Anomaly_pages/footage_3.html')

def foot_4(request):
    return render(request, 'Anomaly_pages/footage_4.html')

def anomaly(request):
    return render(request, 'websites/anomaly.html')





def process_video(request, footage_type):
    global uploaded_video_path
    result_message = None
    uploaded_video_url = None

    if request.method == 'POST':
        form = VideoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.cleaned_data['video_file']
            filename = f"{uuid.uuid4()}.mp4"
            upload_path = os.path.join(settings.MEDIA_ROOT, 'uploads', filename)
            os.makedirs(os.path.dirname(upload_path), exist_ok=True)

            with open(upload_path, 'wb+') as dest:
                for chunk in video.chunks():
                    dest.write(chunk)

            uploaded_video_path = upload_path
            uploaded_video_url = settings.MEDIA_URL + 'uploads/' + filename
            result_message = "✅ Video uploaded! Scroll to see detection stream."
    else:
        form = VideoUploadForm()

    return render(request, 'Anomaly_pages/footage_2.html', {
        'form': form,
        'result_message': result_message,
        'uploaded_video_url': uploaded_video_url
    })

from django.shortcuts import render
from .models import TrafficData
from .forms import VideoUploadForm
import uuid
import os
from django.conf import settings

def foot_1(request):
    global uploaded_video_path
    result_message = None
    uploaded_video_url = None

    # Fetch all locations from TrafficData
    locations = TrafficData.objects.all()

    location_details = None

    if request.method == 'POST':
        # Handle location selection
        location_id = request.POST.get('location')
        if location_id:
            location_details = TrafficData.objects.get(id=location_id)

        # Handle video upload
        form = VideoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.cleaned_data['video_file']
            filename = f"{uuid.uuid4()}.mp4"
            upload_path = os.path.join(settings.MEDIA_ROOT, 'uploads', filename)
            os.makedirs(os.path.dirname(upload_path), exist_ok=True)

            with open(upload_path, 'wb+') as dest:
                for chunk in video.chunks():
                    dest.write(chunk)

            uploaded_video_path = upload_path
            uploaded_video_url = settings.MEDIA_URL + 'uploads/' + filename
            result_message = "✅ Video uploaded! Scroll to see detection stream."

    else:
        form = VideoUploadForm()

    return render(request, 'Anomaly_pages/footage_1.html', {
        'form': form,
        'result_message': result_message,
        'uploaded_video_url': uploaded_video_url,
        'locations': locations,  # Pass all locations to the template
        'location_details': location_details,  # Pass the selected location details to the template
    })
    
def foot_2(request):
    global uploaded_video_path
    result_message = None
    uploaded_video_url = None

    if request.method == 'POST':
        form = VideoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.cleaned_data['video_file']
            filename = f"{uuid.uuid4()}.mp4"
            upload_path = os.path.join(settings.MEDIA_ROOT, 'uploads', filename)
            os.makedirs(os.path.dirname(upload_path), exist_ok=True)

            with open(upload_path, 'wb+') as dest:
                for chunk in video.chunks():
                    dest.write(chunk)

            uploaded_video_path = upload_path
            uploaded_video_url = settings.MEDIA_URL + 'uploads/' + filename
            result_message = "✅ Video uploaded! Scroll to see detection stream."
    else:
        form = VideoUploadForm()
    
    message = ""

    if is_smoke:
        message += 'Smoke Detected'
    
    if is_fire:
        message += ' Fire Detected'

    return render(request, 'Anomaly_pages/footage_2.html', {
        'form': form,
        'result_message': result_message,
        'uploaded_video_url': uploaded_video_url
    })


def foot_3(request):
    global uploaded_video_path
    result_message = None
    uploaded_video_url = None

    if request.method == 'POST':
        form = VideoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.cleaned_data['video_file']
            filename = f"{uuid.uuid4()}.mp4"
            upload_path = os.path.join(settings.MEDIA_ROOT, 'uploads', filename)
            os.makedirs(os.path.dirname(upload_path), exist_ok=True)

            with open(upload_path, 'wb+') as dest:
                for chunk in video.chunks():
                    dest.write(chunk)

            uploaded_video_path = upload_path
            uploaded_video_url = settings.MEDIA_URL + 'uploads/' + filename
            result_message = "✅ Video uploaded! Scroll to see detection stream."
    else:
        form = VideoUploadForm()
    
    message = ""

    if is_smoke:
        message += 'Smoke Detected'
    
    if is_fire:
        message += ' Fire Detected'

    return render(request, 'Anomaly_pages/footage_3.html', {
        'form': form,
        'result_message': result_message,
        'uploaded_video_url': uploaded_video_url
    })

def foot_4(request):
    global uploaded_video_path
    result_message = None
    uploaded_video_url = None

    if request.method == 'POST':
        form = VideoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.cleaned_data['video_file']
            filename = f"{uuid.uuid4()}.mp4"
            upload_path = os.path.join(settings.MEDIA_ROOT, 'uploads', filename)
            os.makedirs(os.path.dirname(upload_path), exist_ok=True)

            with open(upload_path, 'wb+') as dest:
                for chunk in video.chunks():
                    dest.write(chunk)

            uploaded_video_path = upload_path
            uploaded_video_url = settings.MEDIA_URL + 'uploads/' + filename
            result_message = "✅ Video uploaded! Scroll to see detection stream."
    else:
        form = VideoUploadForm()

    return render(request, 'Anomaly_pages/footage_4.html', {
        'form': form,
        'result_message': result_message,
        'uploaded_video_url': uploaded_video_url
    })



def gen_frames_from_uploaded(footage_type):
    global uploaded_video_path, is_fire, is_smoke, is_accident
    cap = cv2.VideoCapture(uploaded_video_path)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Use the correct model based on footage type
        if footage_type == 'fire':
            results = model.predict(source=frame, save=False)
        elif footage_type == 'accident':
            results = model2.predict(source=frame, save=False)

        # Detect fire or accident based on the model results
        if footage_type == 'fire':
            for i in results:
                f = [int(j) for j in i.boxes.cls]
                is_fire = f.count(2)  # Detect fire

            annotated = results[0].plot()
            if is_fire:
                text = "Fire Detected, Kindly take action"
                font = cv2.FONT_HERSHEY_SIMPLEX
                position = (50, 50)
                cv2.putText(annotated, text, position, font, 1, (0, 255, 0), 2)

        elif footage_type == 'accident':
            for i in results:
                f = [int(j) for j in i.boxes.cls]
                is_accident = f.count(5)  # Detect accident

            annotated = results[0].plot()
            if is_accident:
                text = "Accident Detected, Kindly take action"
                font = cv2.FONT_HERSHEY_SIMPLEX
                position = (50, 50)
                cv2.putText(annotated, text, position, font, 1, (0, 255, 0), 2)

        _, jpeg = cv2.imencode('.jpg', annotated)
        frame_bytes = jpeg.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')
    cap.release()


def video_feed_uploaded(request):
    return StreamingHttpResponse(gen_frames_from_uploaded(), content_type='multipart/x-mixed-replace; boundary=frame')

def video_feed_uploaded(request, footage_type='accident'):
    return StreamingHttpResponse(gen_frames_from_uploaded(footage_type), content_type='multipart/x-mixed-replace; boundary=frame')


def detect():
    if is_fire:
        yield "Fire Detected <br>"
    if is_accident:
        yield "Accident Detected <br>"


def alert_update(request):
    return StreamingHttpResponse(detect(), content_type='text/event-stream')

@login_required
def anomaly(request):
    # Fetch all locations from TrafficData
    locations = TrafficData.objects.all()

    location_details = None
    # Handle POST request
    if request.method == 'POST':
        # Get the selected location ID from the form
        location_id = request.POST.get('location')
        if location_id:
            # Retrieve the location details
            location_details = TrafficData.objects.get(id=location_id)

    # Send the selected location details and list of locations to the template
    return render(request, 'websites/anomaly.html', {
        'locations': locations,
        'location_details': location_details
    })
def fetch_authorities(request):
    if request.method == 'POST':
        location_id = request.POST.get('location')
        location = TrafficData.objects.get(id=location_id)

        # Get the contact details
        police_contact = location.police_contact
        hospital_contact = location.hospital_contact
        fire_contact = location.fire_contact

        # Pass the contact details to the footage_1 page
        return render(request, 'Anomaly_pages/footage_1.html', {
            'police_contact': police_contact,
            'hospital_contact': hospital_contact,
            'fire_contact': fire_contact,
        })

from django.http import JsonResponse
from .forms import IncidentReportForm

def create_incident_report(request):
    if request.method == 'POST':
        form = IncidentReportForm(request.POST)

        if form.is_valid():
            # Save the form data to the database
            incident_report = form.save()

            # Return a success response with the incident report details
            return JsonResponse({
                'success': True,
                'message': 'Incident report submitted successfully!',
                'incident': {
                    'incident_id': incident_report.incident_id,
                    'date': incident_report.date,
                    'location': incident_report.location,
                    'description': incident_report.description,
                    'status': incident_report.status
                }
            })
        else:
            # Return error response if form is invalid
            return JsonResponse({'success': False, 'message': 'Error in form submission!', 'errors': form.errors})

    # If the method is not POST, return error
    return JsonResponse({'success': False, 'message': 'Invalid request method.'})

