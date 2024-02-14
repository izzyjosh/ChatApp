from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("chat/",include("main.urls")),
    path('accounts/', include('allauth.urls')),
    path("auth/",include("accapp.urls")),
]
