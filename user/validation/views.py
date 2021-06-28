from django.shortcuts import render, redirect
from validation.models import user
from django.contrib import messages
from . import models
import re


def index(request):
    return render(request, 'login.html')


def reg(request):
    return render(request, 'registration.html')


def signUp(request):
    if request.method == "POST":
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password != cpassword:
            messages.info(request, 'Password not match in both field.')
            return redirect("registration")
        elif len(password) < 8:
            messages.info(request, 'Password must be atleast 8 characters.')
            return redirect("registration")
        elif not((re.search("[^a-zA-Z0-9]+", password) != None) and (re.search("[a-z]+", password) != None) and (re.search("[A-Z]+", password) != None) and (re.search("[0-9]+", password) != None)):
            messages.info(
                request, 'Password must contain Upper Lower digit and special symbol')
            return redirect("registration")
        else:
            ins = user(first_name=first_name,
                       last_name=last_name, email=email, password=password)
            ins.save()
            messages.success(request, 'Successfully SIGN UP')
            return redirect("/")
    else:
        return render(request, 'registration.html')


def logIn(request):
    if request.method == "POST":
        user = request.POST['username']
        psw = request.POST['password']
        userData = models.user.objects.all()
        for Data in userData:
            if user in Data.email and psw in Data.password:
                return render(request, "userDetails.html", {'Data': Data})
        messages.success(request, 'Not Valid user')
        return redirect('/')
    else:
        return render(request, 'login.html')
