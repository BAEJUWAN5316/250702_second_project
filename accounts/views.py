from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.generic import CreateView

# 회원가입
register = CreateView.as_view(
    form_class=UserCreationForm,
    template_name="accounts/register.html",
    success_url="/auth/login/"
)

#로그인, 로그아웃

login = LoginView.as_view(next_page="/")
logout = LogoutView.as_view(next_page="/")

