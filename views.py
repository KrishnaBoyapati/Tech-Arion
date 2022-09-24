from django.shortcuts import render
from .models import*
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


from django.views.generic import CreateView
from rest_framework import views






# Create your views here.
def first_page(request):
    pipes = MainPage.objects.all()
    data_array=[]
    for data in pipes:
        data_details = {}
        data_details['Id'] = data.page_id
        data_details['Name'] = data.name
        data_details['Description'] = data.description
        data_details['Image'] = data.product_image
        data_details['Thickness'] = data.thickness
        data_details['Size'] = data.size
        data_details['Rating'] = data.rating
        data_array.append(data_details)
    return JsonResponse({'response': {"response_code": '200', 'data': data_array}})

# api to get technician details and edit the technician
@csrf_exempt
def second_page(request):
    data = json.loads(request.body)
    pipes = MainPage.objects.get(pk=data['id'])
    data_details = {}
    data_details['Name'] = pipes.name
    data_details['Description'] = pipes.description
    data_details['Image'] = pipes.product_image
    data_details['Thickness'] = pipes.thickness
    data_details['Size'] = pipes.size
    data_details['Rating'] = pipes.rating
    return JsonResponse({'response': {"response_code": '200', 'data': data_details}})