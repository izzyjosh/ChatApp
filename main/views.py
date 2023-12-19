from django.shortcuts import render,redirect
from django.http import HttpRequest


def index(request:HttpRequest):
    return render(request,"main/index.html")
