from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import ProfileCreationForm, ProfileChangeForm
from .models import Profile, Address
# Register your models here.
class ProfileUserAdmin(UserAdmin):
    add_form = ProfileCreationForm
    form = ProfileChangeForm
    model= Profile
    #to display the fields in model in admin
    list_display = ('name','email','profile_pic','phone_number',)
    # to filter records based on the given fields
    list_filter = ('gender','address__city')

    #To see and update the fields in admin
    fieldsets = (
        (None,{'fields':('email','password','phone_number')}),
        ('Permissions',{'fields':('is_staff','is_active')}),
    )

    #To see the fields while adding new records in admin
    add_fieldsets = (
        (None,{
            'classes':('wide',),
            'fields':('name','email','password1','password2','phone_number','gender','date_of_birth','is_staff','is_active',)
        }),
    )
    #to search record with given field
    search_fields = ('name',)
    ordering = ('name',)

admin.site.register(Address)
admin.site.register(Profile, ProfileUserAdmin)