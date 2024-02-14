from django.shortcuts import render
from django.contrib.auth import get_user_model
from .forms import UserRegistrationForm

User = get_user_model()

def signup(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            form.save()
        else:
            print("error")

    else:
        form = UserRegistrationForm()

    return render(request,"account/signup.html",{"form":form})


