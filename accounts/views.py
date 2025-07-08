from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect
from .forms import UserProfileForm, CustomPasswordChangeForm, TraitSurveytForm
from .utils import generate_trait
from accounts.models import UserProfile

# 회원가입
register = CreateView.as_view(
    form_class=UserCreationForm,
    template_name="accounts/register.html",
    success_url="/auth/login/"
)

#로그인, 로그아웃

login = LoginView.as_view(next_page="/")
logout = LogoutView.as_view(next_page="/")


# 프로필변경, 비밀번호 변경
@login_required
def profile_main(request):
    profile, _ = UserProfile.objects.get_or_create(user=request.user)
    return render(
        request,
        "accounts/profile.html",
        {"profile":profile}
    )

@login_required
def profile_edit(request):
    profile, _ = UserProfile.objects.get_or_create(user=request.user)
    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = UserProfileForm(instance=profile)

    return render(
        request,
        "accounts/profile_edit.html",
        {"form": form}
    )

@login_required
def password_change(request):
    if request.method == "POST":
        form = CustomPasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect("profile")
    else:
        form = CustomPasswordChangeForm(user=request.user)
    
    return render(
        request,
        "accounts/password_change.html",
        {"form":form}
    )


@login_required
def assign_trait(request):
    profile, _ = UserProfile.objects.get_or_create(user=request.user)

    if profile.trait:
        return redirect("profile")
    
    if request.method == "POST":
        form = TraitSurveytForm(request.POST)
        if form.is_valid():
            q1 = form.cleaned_data["q1"]
            q2 = form.cleaned_data["q2"]
            q3 = form.cleaned_data["q3"]

            trait = generate_trait(q1, q2, q3)
            profile.trait = trait
            profile.save()
            return redirect("profile")
    
    else:
        form = TraitSurveytForm()

    return render(
        request,
        "accounts/assign_trait.html",
        {"form":form}
    )