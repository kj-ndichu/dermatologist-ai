from django.shortcuts import render, redirect
import shutil
import os
import easygui
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from . import predict
from .forms import UserRegisterForm
from django.contrib import messages


def home(request):

    if request.method == "GET":
        return render(request, 'login.html')


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Hi {username}, your account was created successfully!')
            return redirect('skin_app:login')
    else:
        form = UserRegisterForm()

    return render(request, 'register.html', {'form': form})


@csrf_exempt
def submit(request):
    if request.method == "POST":
        image = request.FILES['image']
        shutil.rmtree(os.getcwd()+'//static//img')
        path = default_storage.save(
            os.getcwd()+'//static//img//result.jpg', ContentFile(image.read()))
        tmp_file = os.path.join(settings.MEDIA_ROOT, path)
        result = predict.process()
        result = result.split('/')
        f = open(os.path.dirname(__file__)+"/session.txt", "r+")
        name = f.read()
        f.close()
        return render(request, 'result.html', {"result": result[0], 'name': name, 'description': result[1]})


def dashboard(request):
    if request.method == 'GET':
        return render(request, 'index.html')


def profile(request):
    return render(request, 'profile.html')
