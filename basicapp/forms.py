from django import forms
from django.contrib.auth.models import User
from basicapp.models import UserProfileInfo

class userform(forms.ModelForm):
    # password = forms.CharField(widget=forms.PasswordInput , max_length=244 )
    
    class Meta():
        model = User
        fields = ('username','email')
    
class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('profile_pic',)