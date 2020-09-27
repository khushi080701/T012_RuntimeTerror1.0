from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
import json
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import Crop

# Create your views here.

def home(request):
    return render(request, 'codeit.html')
def requirements(request):
    return render(request, 'requirements.html')
def addProduct(request):
    return render(request, 'addProduct.html')

def signUp(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signUp.html', {'form': form})

def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password=request.POST['password1']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            return redirect('signUp')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login')
    else:
        return render(request,'login.html')
def req(request):
    crop = Crop.objects.all()
    return render(request,'crop.html', {'crop':crop})
