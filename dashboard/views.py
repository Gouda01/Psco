from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required



# Create your views here.
def website (request) :
    return render (request, 'website.html')


@login_required
def dashboard (request):
    return render (request, 'dashboard.html')