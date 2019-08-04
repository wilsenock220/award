from __future__ import unicode_literals
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404


def index(request):
    return render(request, 'index.html', locals())


def home(request):
    return render(request, 'home.html', locals())
