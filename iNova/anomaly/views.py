from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os
from .yolo_fire import run_fire_detection

# def anomaly(request):
#     return render(request, 'websites/anomaly.html')

def anomaly(request):
    return render(request, 'websites/fire_detection.html')

def fire_detection(request):
    return render(request, 'websites/fire_detection.html')

def upload_fire_video(request):
    context = {}
    if request.method == 'POST' and request.FILES.get('video'):
        video = request.FILES['video']
        fs = FileSystemStorage()
        input_path = fs.save(f'input/{video.name}', video)
        full_input_path = fs.path(input_path)
        
        print(f"Input video saved to: {full_input_path}")
        
        output_dir = os.path.join(settings.MEDIA_ROOT, 'output')
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, f'detected_{video.name}')
        
        print(f"Output directory: {output_dir}")
        
        detected_path = run_fire_detection(full_input_path, output_path)
        
        if detected_path and os.path.exists(detected_path):
            context['input_video_url'] = fs.url(input_path)
            
            # Convert the detected_path to a URL
            relative_path = os.path.relpath(detected_path, settings.MEDIA_ROOT)
            # Replace backslashes with forward slashes for URLs
            relative_path = relative_path.replace('\\', '/')
            context['output_video_url'] = f"{settings.MEDIA_URL}{relative_path}"
            
            print(f"Input URL: {context['input_video_url']}")
            print(f"Output URL: {context['output_video_url']}")
        else:
            context['error'] = "Failed to process the video. Please try again."
            print(f"Detection failed. detected_path: {detected_path}")

    return render(request, 'websites/fire_detection.html', context)
