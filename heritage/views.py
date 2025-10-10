from django.shortcuts import render
from .models import *
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect


def welcome(request):
  return render(request, "welcome.html")

def index(request):
  return render(request, "index.html")