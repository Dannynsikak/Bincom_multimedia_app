from django.shortcuts import render, redirect

# Create your views here.
from .models import MediaFile
from .Uploadform import MediaUploadForm


def media_list(request):
    media_files = MediaFile.objects.all()
    return render(request, 'media_app/media_list.html', {'media_files': media_files})


def upload_media(request):
    if request.method == 'POST':
        form = MediaUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('media_list')
    else:
        form = MediaUploadForm()
    return render(request, 'media_app/upload_media.html', {'form': form})
