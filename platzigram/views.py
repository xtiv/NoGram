""" Platzigram views"""
import json


# Django
from django.http import HttpResponse

# Utilities
from datetime import datetime

def hello_world(request):
    """
    Return a greeting
    """
    
    # No se puede enviar la variable con la fecha, hay que castearlo a str
    return HttpResponse("Oh, hi! Current server time is {now}".format(now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs')))

def sort_integers(request):
    """
    Return a JSON response with sorted integers
    """
    numbers = sorted([int(number) for number in request.GET['numbers'].split(',')])
    response = json.dumps({
        "status": "ok",
        "numbers": numbers,
        "messaje" : "The list is sorted"
        }, indent=4)
    return HttpResponse(f"{response}")

def say_hi(request, name, age):
    """Return a greeting but this function has a condiotional"""
    if age < 12:
        message = f'Sorry {name}, u are not allowed here'
    else:
        message = f'Hello {name}! Welcome to Platzigram'
    
    return HttpResponse(message)
    