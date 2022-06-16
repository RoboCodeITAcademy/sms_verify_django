from django.shortcuts import render
from django.http import JsonResponse
import requests
# Create your views here.

TOKEN = "b68cc43a07a1a9ebe2a978990f28a1a7"
DEVICE_ID = 315565


def sender(request):
    # return JsonResponse({"status": 200})
    return render(request, "index.html")
