from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os

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

def traffic(request):
    video_1_url = None
    video_2_url = None
    video_3_url = None
    video_4_url = None

    if request.method == 'POST':
        fs = FileSystemStorage()

        # Handle video uploads
        if 'video_1' in request.FILES:
            video_1 = request.FILES['video_1']
            video_1_name = fs.save(f'videos/{video_1.name}', video_1)
            video_1_url = fs.url(video_1_name)

        if 'video_2' in request.FILES:
            video_2 = request.FILES['video_2']
            video_2_name = fs.save(f'videos/{video_2.name}', video_2)
            video_2_url = fs.url(video_2_name)

        if 'video_3' in request.FILES:
            video_3 = request.FILES['video_3']
            video_3_name = fs.save(f'videos/{video_3.name}', video_3)
            video_3_url = fs.url(video_3_name)

        if 'video_4' in request.FILES:
            video_4 = request.FILES['video_4']
            video_4_name = fs.save(f'videos/{video_4.name}', video_4)
            video_4_url = fs.url(video_4_name)

    return render(request, 'websites/traffic.html', {
        'video_1_url': video_1_url,
        'video_2_url': video_2_url,
        'video_3_url': video_3_url,
        'video_4_url': video_4_url,
    })
