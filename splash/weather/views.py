curr_cap_value = 0.4
prev_cap_value = 1.5
next_cap_value = 1.5
interval = 10

import json
import os
import json
import requests
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
clientID = 1
def createCron(nextCall, clientID):
    os.system(f'python3 cron.py {clientID}')

def ask_sprinkle(request):
    next_call = interval
    if currentlyRaining():
        # do not start sprinkler
        print("Currently raining, do not start sprinkler.")
        createCron(next_call, clientID)
        return HttpResponse(False)
    return HttpResponse("asd")

def currentlyRaining():
    '''
        Function returns True if the rain currently is falling more then 0.4 mm 
    '''
    # precip_mm 
    current_file = "current_raining.json"
    my_file = open(current_file,"r")
    dummy_data = json.load(my_file)
    if dummy_data['current']['precip_mm'] > curr_cap_value:
        print("Rain has fallen more than 0.4 mm CURRENTLY.")
        return True
    return False

def didRain():
    '''
        Function returns True if the rain previously fell more then 1.5 mm 
    '''
    # totalprecip_mm
    previous_file = "previous_raining.json"
    endpointURL = 'https://api.weatherapi.com/v1/history.json?key=a4b36c3290e34a97aae133608220610&q=23.062459600418087,72.67048492141697&dt=2022-10-06'
    apiResponse = requests.get(endpointURL).json()
    my_file = open(previous_file,"r")
    dummy_data = json.load(my_file)
    # if apiResponse["current"]["precip_mm"] == 0.0:
    #     return False
    if dummy_data['forecast']['forecastday'][0]['day']['totalprecip_mm'] > prev_cap_value:
        print("Rain has fallen more than 1.5 mm PREVIOUSLY.")
        return True
    return False

def willRain():
    '''
        Function returns True if the rain next will fall more then 1.5 mm 
    '''
    # totalprecip_mm
    next_file = "next_raining.json"
    endpointURL = 'https://api.weatherapi.com/v1/forecast.json?key=a4b36c3290e34a97aae133608220610&q=23.529769486962326,72.45743588980896'
    apiResponse = requests.get(endpointURL).json()
    my_file = open(next_file,"r")
    dummy_data = json.load(my_file)
    # dummy_data['forecast'][0]['totalprecip_mm']
    if dummy_data['forecast']['forecastday'][0]['day']['totalprecip_mm'] > next_cap_value: 
        print("Rain will fall more than 1.5 mm NEXT.")
        return True
    return False
