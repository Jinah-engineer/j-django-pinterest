from django.forms import ModelForm

from profileapp.models import Profile

# extends 'ModelForm'
class ProfileCreationForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'nickname', 'message']

        