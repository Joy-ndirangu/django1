from django.contrib import admin
from .models import Students, Sliders


from django.contrib.auth.admin import UserAdmin
from teachers.models import CustomUser
from teachers.form import CustomUserCreationForm,CustomUserChangeForm


# After importing the models, Register your models here.

admin.site.register(Students)
admin.site.register(Sliders)


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

admin.site.register(CustomUser, CustomUserAdmin)