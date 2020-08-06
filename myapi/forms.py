from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Profile

class ProfileCreationForm(UserCreationForm):
    class Meta():
        model = Profile
        fields = ('email',)
class ProfileChangeForm(UserChangeForm):
    class Meta():
        model = Profile
        fields = ('email',)