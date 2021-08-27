from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
from django.template import loader
from .models import Ressource


def index(request):
    ressource_list = Ressource.objects.all()
    return render(request, 'ressources/index.html', {'ressource_list': ressource_list})


def detail(request, res_id):
    ressource = get_object_or_404(Ressource, pk=res_id)
    return render(request, 'ressources/detail.html', {'ressource': ressource})
