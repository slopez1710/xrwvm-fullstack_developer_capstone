from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
import logging
import json
from .models import CarMake, CarModel

from .populate import initiate

logger = logging.getLogger(__name__)

@csrf_exempt
def login_user(request):
    data = json.loads(request.body)
    username = data['userName']
    password = data['password']

    user = authenticate(username=username, password=password)
    response = {"userName": username}

    if user is not None:
        login(request, user)
        response["status"] = "Authenticated"

    return JsonResponse(response)

def logout_request(request):
    logout(request)
    return JsonResponse({"status": "Logged out successfully"})

@csrf_exempt
def registration(request):
    data = json.loads(request.body)
    username = data['userName']
    password = data['password']
    first_name = data['firstName']
    last_name = data['lastName']

    try:
        User.objects.get(username=username)
        return JsonResponse({"userName": username, "status": "User already exists"})
    except User.DoesNotExist:
        user = User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password
        )
        login(request, user)
        return JsonResponse({"userName": username, "status": "User created successfully"})

def get_dealerships(request):
    if request.method == "GET":
        dealerships = initiate()
        return JsonResponse(dealerships, safe=False)

def get_dealer_reviews(request, dealer_id):
    if request.method == "GET":
        reviews = initiate()
        return JsonResponse(reviews, safe=False)

def get_dealer_details(request, dealer_id):
    if request.method == "GET":
        dealer = initiate()
        return JsonResponse(dealer, safe=False)

@csrf_exempt
def add_review(request):
    if request.method == "POST":
        data = json.loads(request.body)
        review = initiate()
        return JsonResponse({"status": "Review submitted successfully"})
def get_cars(request):
    count = CarMake.objects.filter().count()
    print(count)
    if(count == 0):
        initiate()
    car_models = CarModel.objects.select_related('car_make')
    cars = []
    for car_model in car_models:
        cars.append({"CarModel": car_model.name, "CarMake": car_model.car_make.name})
    return JsonResponse({"CarModels":cars})

