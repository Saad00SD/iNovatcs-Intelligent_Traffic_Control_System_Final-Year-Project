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


# v2
def upload_fire_video(request):
    context = {}
    if request.method == 'POST' and request.FILES.get('video'):
        video = request.FILES['video']
        fs = FileSystemStorage()

        # Save uploaded video to 'input' directory within MEDIA_ROOT
        input_filename = fs.save(f'input/{video.name}', video)
        full_input_path = fs.path(input_filename)

        # Ensure 'output' directory exists
        output_dir = os.path.join(settings.MEDIA_ROOT, 'output')
        os.makedirs(output_dir, exist_ok=True)

        output_filename = f'detected_{video.name.split(".")[0]}.mp4'  # Ensure it saves as .mp4
        full_output_path = os.path.join(output_dir, output_filename)

        # Process the video
        detected_path = run_fire_detection(full_input_path, full_output_path)

        if detected_path and os.path.exists(detected_path):
            # Prepare URLs for the template
            context['input_video_url'] = fs.url(input_filename)
            relative_output_path = os.path.relpath(detected_path, settings.MEDIA_ROOT)
            context['output_video_url'] = f"{settings.MEDIA_URL}{relative_output_path.replace(os.sep, '/')}"
        else:
            context['error'] = "Failed to process the video. Please try again."

    return render(request, 'websites/fire_detection.html', context)