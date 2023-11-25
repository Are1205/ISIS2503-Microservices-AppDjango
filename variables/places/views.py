from .models import Place
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse
from django.http import JsonResponse
import json

def placesleList(request):
    queryset = Variable.objects.all()
    context = list(queryset.values('id', 'name'))
    return JsonResponse(context, safe=False)

def placesCreate(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        variable = Place()
        variable.name = data_json["name"]
        variable.save()
        return HttpResponse("successfully created place")