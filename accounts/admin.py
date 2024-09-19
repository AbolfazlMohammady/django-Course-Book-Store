from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User
from .forms import UserChangeForm, UserCreationForm

@admin.register(User)
class UserAdmin(UserAdmin):

    model= User
    form= UserChangeForm
    fields= UserAdmin.fields
    add_form= UserCreationForm
    # list_display= UserAdmin.list_display + ('age',)
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ('age',),}),
        )
    add_fieldsets= UserAdmin.add_fieldsets + (
        (None, {"fields": ('age',),}),
        )
    
