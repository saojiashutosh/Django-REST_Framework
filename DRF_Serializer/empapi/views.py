from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from rest_framework import serializers

# Create your views here.
def home(request):
    return