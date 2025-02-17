from django.shortcuts import render, redirect

# Create your views here.
from .models import MediaFile
from .Uploadform import MediaUploadForm
from django.http import HttpResponseNotAllowed


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
    
def delete_media(request, media_id):
    if request.method == 'POST':
        try:
            media_file = MediaFile.objects.get(id=media_id)
            media_file.delete()
            return redirect('media_list')
        except MediaFile.DoesNotExist:
            return redirect('media_list')
    else:
        return HttpResponseNotAllowed(['POST'])