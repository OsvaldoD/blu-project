from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import AplicaCreditoForm, MessageForm
from .models import Message
from django.contrib import messages

from .models import *

# Create your views here.


def index(request):
    form = MessageForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        message = form.save(commit=False)

        message.save()

    return render(request, 'bluApp/index.html', context)


def save(request):
    return render(request, 'bluApp/save.html')


def transact(request):
    return render(request, 'bluApp/transact.html')


def loan(request):
    return render(request, 'bluApp/loan.html')


# @login_required(login_url="user:login")
def aplica_credito(request):
    form = AplicaCreditoForm(request.POST or None)
    if form.is_valid():
        credito = form.save(commit=False)

        credito.author = request.user
        credito.save()
        messages.success(request, "Aplicacao de credito submeticdo com sucesso")
        return redirect("bluApp:index")


    return render(request, "bluApp/loan.html", {"form": form})