from django import forms

class VideoUploadForm(forms.Form):
    video_file_1 = forms.FileField(label='Upload Video 1', required=True)
    video_file_2 = forms.FileField(label='Upload Video 2', required=True)
    video_file_3 = forms.FileField(label='Upload Video 3', required=True)
    video_file_4 = forms.FileField(label='Upload Video 4', required=True)
