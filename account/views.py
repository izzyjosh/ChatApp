from django.shortcuts import render,redirect
from .forms import UserRegistrationForm
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required


def signup(request:HttpRequest):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("account:login")

    else:
        form = UserRegistrationForm()

    return render(request,"account/signup.html",{"form":form})
