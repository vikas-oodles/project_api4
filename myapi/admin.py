from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import ProfileCreationForm, ProfileChangeForm
from .models import Profile, Address
# Register your models here.
class ProfileUserAdmin(UserAdmin):
    add_form = ProfileCreationForm
    form = ProfileChangeForm
    model= Profile
    list_display = ('name','email','profile_pic','phone_number',)
    list_filter = ('gender','address__city')

    fieldsets = (
        (None,{'fields':('email','password')}),
        ('Permissions',{'fields':('is_staff','is_active')}),
    )
    add_fieldsets = (
        (None,{
            'classes':('wide',),
            'fields':('email','password1','password2','is_staff','is_active')
        }),
    )
    search_fields = ('name',)
    ordering = ('name',)

admin.site.register(Address)
admin.site.register(Profile, ProfileUserAdmin)