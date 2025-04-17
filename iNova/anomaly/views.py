from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os
from .yolo_fire import run_fire_detection
from ultralytics import YOLO
import os
import pandas
import time
model  = YOLO(r'anomaly/MLModels/best.pt')


from django.shortcuts import render


# def anomaly(request):
#     return render(request, 'websites/anomaly.html')

from django.shortcuts import render

# Views for each footage
def foot_1(request):
    return render(request, 'Anomaly_pages/footage_1.html')

def foot_2(request):
    return render(request, 'Anomaly_pages/footage_2.html')

def foot_3(request):
    return render(request, 'Anomaly_pages/footage_3.html')

def foot_4(request):
    return render(request, 'Anomaly_pages/footage_4.html')


from django.shortcuts import render
from django.http import StreamingHttpResponse
from django.conf import settings
from .forms import VideoUploadForm
import os, uuid, cv2

uploaded_video_path = None  # global var for streaming
is_fire  = False
is_smoke = False


def foot_1(request):
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

    return render(request, 'Anomaly_pages/footage_1.html', {
        'form': form,
        'result_message': result_message,
        'uploaded_video_url': uploaded_video_url,
        'message': message
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



def gen_frames_from_uploaded():
    global uploaded_video_path
    global is_fire, is_smoke
    cap = cv2.VideoCapture(uploaded_video_path)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        results = model.predict(source=frame, save=False)
        
        for i in results:
            f = [int(j) for j in i.boxes.cls]
            print("Fires:", f.count(2))
            is_fire = f.count(2)

        annotated = results[0].plot()
        if is_fire:
            text = "Fire Detected, Kindly take action"
            font = cv2.FONT_HERSHEY_SIMPLEX
            font_scale = 1
            color = (0, 255, 0)
            thickness = 2
            position = (50, 50)

            cv2.putText(annotated, text, position, font, font_scale, color, thickness)

        _, jpeg = cv2.imencode('.jpg', annotated)
        frame_bytes = jpeg.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')
    cap.release()

def video_feed_uploaded(request):
    return StreamingHttpResponse(gen_frames_from_uploaded(), content_type='multipart/x-mixed-replace; boundary=frame')


def detect():
    if is_fire:
        yield "Fire Detected <br>"

def alert_update(request):
    return StreamingHttpResponse(detect(), content_type='text/event-stream')




def anomaly(request):
    return render(request, 'websites/anomaly.html')

def fire_detection(request):
    return render(request, 'websites/fire_detection.html')

# def upload_fire_video(request):
#     context = {}
#     if request.method == 'POST' and request.FILES.get('video'):
#         video = request.FILES['video']
#         fs = FileSystemStorage()
#         input_path = fs.save(f'input/{video.name}', video)
#         full_input_path = fs.path(input_path)
        
#         print(f"Input video saved to: {full_input_path}")
        
#         output_dir = os.path.join(settings.MEDIA_ROOT, 'output')
#         os.makedirs(output_dir, exist_ok=True)
#         output_path = os.path.join(output_dir, f'detected_{video.name}')
        
#         print(f"Output directory: {output_dir}")
        
#         detected_path = run_fire_detection(full_input_path, output_path)
        
#         if detected_path and os.path.exists(detected_path):
#             context['input_video_url'] = fs.url(input_path)
            
#             # Convert the detected_path to a URL
#             relative_path = os.path.relpath(detected_path, settings.MEDIA_ROOT)
#             # Replace backslashes with forward slashes for URLs
#             relative_path = relative_path.replace('\\', '/')
#             context['output_video_url'] = f"{settings.MEDIA_URL}{relative_path}"
            
#             print(f"Input URL: {context['input_video_url']}")
#             print(f"Output URL: {context['output_video_url']}")
#         else:
#             context['error'] = "Failed to process the video. Please try again."
#             print(f"Detection failed. detected_path: {detected_path}")

#     return render(request, 'websites/fire_detection.html', context)


