from django.shortcuts import render

from django.core.files.storage import FileSystemStorage

# Create your views here.

def upload1(request):
    if request.method == 'post':
        upload_files =request.FILES['document']
        # print(upload_files.name)
        # print(upload_files.size)
    return render(request,'upload.html')