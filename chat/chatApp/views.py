from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "index.html")


def post_queries(request):
    if request.method == "POST":
        print("Data recieved", request)
        return JsonResponse(request)
