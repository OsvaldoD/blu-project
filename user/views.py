from django.shortcuts import render,redirect
from .forms import LoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.


def login_user(request):
    form = LoginForm(request.POST or None)

    context = {
        "form": form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(request, username=username, password=password)

        if user is None:
            messages.info(request, "Nome de usuário ou senha incorreta")
            return render(request, "user/login.html", context)
        # messages.success(request, "Loged Successfully")
        login(request, user)
        if request.user.is_superuser:
           return redirect('/admin/')
        return redirect("/")


    return render(request, 'user/login.html', context)



def logout_user(request):
    logout(request)
    messages.success(request,"Logout successfully")
    return redirect("/")

def dashboard(request):
    return render(request, 'user/dashboard.html')