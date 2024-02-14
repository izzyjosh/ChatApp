from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from django.utils.translation import gettext_lazy as _

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_dusplay = ["username","email"]
    empty_value_display = "--empty--"
    search_fielda = ["username"]
    list_per_page = 100
    date_hierarchy = "date_joined"


    field_set = (
            (None,{"fields": ("username","password")}),
            (_("Personnal Info"),{"fields":("first_name","last_name","email")}),
            (_("Permissions"),{
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",                  
                    )
                }
             ),
            (_("Important Dates"),{"fielda":("last_login","date_joined")}),)

    add_fieldsets = (
            (None, {
                "classes":("wide",),
                "fields": ("username","email","password1","password2")
                }
             ))

