from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth
from django.conf import settings
from accounts.forms import SignupForm


class Loginviews(LoginView):
    template_name = 'login.html'


login = Loginviews.as_view()


class LogoutViews(LogoutView):
    next_page = settings.LOGOUT_REDIRECT_URL


logout = LogoutViews.as_view()


def signup(request):
    """signup
    to register users
    """
    if request.method == "POST":
        signupform = SignupForm(request.POST)
        if signupform.is_valid():
            signupform.save()

            return redirect('home')
    elif request.method == "GET":
        signupform = SignupForm()

    return render(request, "signup.html", {
        "signupform": signupform,
    })