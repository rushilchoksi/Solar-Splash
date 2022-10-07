import json
import os
import requests
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
clientID = 1
def createCron(nextCall, clientID):
    os.system(f'python3 cron.py {clientID}')

def ask_sprinkle(request):
    print("starts")
    currentlyRaining()
    didRain()
    print("end")
    return HttpResponse("asd")

def currentlyRaining():
    endpointURL = 'https://api.weatherapi.com/v1/current.json?key=a4b36c3290e34a97aae133608220610&q=23.016062199507843,72.47214227178155'
    apiResponse = requests.get(endpointURL).json()
    with open('current.json', 'w') as mainFile:
        # mainFile.write(json.dump(apiResponse))
        json.dump(apiResponse,mainFile,indent=4)
    if apiResponse["current"]["precip_mm"] == 0.0:
        return False
    return True

def didRain():
    endpointURL = 'https://api.weatherapi.com/v1/history.json?key=a4b36c3290e34a97aae133608220610&q=23.062459600418087,72.67048492141697&dt=2022-10-06'
    apiResponse = requests.get(endpointURL).json()
    with open('previous.json', 'w') as mainFile:
        # mainFile.write(json.dump())
        json.dump(apiResponse,mainFile,indent=4)
    # if apiResponse["current"]["precip_mm"] == 0.0:
    #     return False
    return True

def willRain():
    return True
