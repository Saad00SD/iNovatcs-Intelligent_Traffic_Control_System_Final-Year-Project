from django.shortcuts import render

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

from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .forms import VideoUploadForm

def footage_1(request):
    context = {}
    if request.method == 'POST':
        video_urls = []
        for i in range(1, 5):
            if f'video_file_{i}' in request.FILES:
                video_file = request.FILES[f'video_file_{i}']
                fs = FileSystemStorage()
                filename = fs.save(video_file.name, video_file)
                video_url = fs.url(filename)
                video_urls.append(video_url)
        
        context['video_urls'] = video_urls

    form = VideoUploadForm()
    context['form'] = form
    return render(request, 'Traffic_page/footage_1.html', context)

