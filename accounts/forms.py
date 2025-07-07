from django import forms
from .models import UserProfile
from django.contrib.auth.forms import PasswordChangeForm

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["nickname", "profile_image"]


class CustomPasswordChangeForm(PasswordChangeForm):
    pass

class TraitSurveytForm(forms.Form):
    q1 = forms.CharField(label="새벽 2시에 가장 친한 친구에게 전화가 왔습니다. 친구는 무슨 말을 할까요?")
    q2 = forms.CharField(label="자고 일어났더니 어제 꿈을 꾼 것 같은데 기억이 잘 나지 않습니다. 기억을 더듬어보니 조금 생각날 것 같습니다. 무슨 꿈인가요?")
    q3 = forms.CharField(label="길을 걷다 보니 바닥에 돈이 떨어져 있습니다. 얼마가 떨어져 있었나요?")