from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView
from .models import MyUser

from .forms import UserSignUpForm, UserLoginForm, PatientSignUp


def signup(request, *args, **kwargs):
    patient_form = PatientSignUp(request.POST)
    form = UserSignUpForm(request.POST or None)
    if form.is_valid() and patient_form.is_valid():
        user = form.save()

        patient = patient_form.save(commit=False)
        patient.user = user

        patient.save()

        return HttpResponseRedirect('/accounts/login/')
    context = {
        "form": form,
        'patient_form': patient_form,
    }
    return render(request, 'registration/signup.html', context)


def login_view(request, *args, **kwargs):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        user_obj = form.cleaned_data.get('user_obj')
        login(request, user_obj)
        return HttpResponseRedirect('/')
    return render(request, 'registration/login.html', {'form': form})


def logout_view(request, *args, **kwargs):
    logout(request)
    return HttpResponseRedirect('/accounts/login/')
