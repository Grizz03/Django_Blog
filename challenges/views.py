from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


# Create your views here.

def month_challenge(request, month):
    challenge_text = None  # Declare text to None to have no value
    if month == 'january':  # Iterate over each route the user can access and what should be displayed
        challenge_text = 'Get a dev job in January ^.^'  # Change values with each route(month)
    elif month == 'february':
        challenge_text = 'Get a dev job in February ^.^'
    elif month == 'march':
        challenge_text = 'Get a dev job in March ^.^'
    elif month == 'april':
        challenge_text = 'Get a dev job in April ^.^'
    elif month == 'may':
        challenge_text = 'Get a dev job in May ^.^'
    elif month == 'june':
        challenge_text = 'Get a dev job in June ^.^'
    elif month == 'july':
        challenge_text = 'Get a dev job in July ^.^'
    elif month == 'august':
        challenge_text = 'Get a dev job in August ^.^'
    elif month == 'september':
        challenge_text = 'Get a dev job in September ^.^'
    elif month == 'october':
        challenge_text = 'Get a dev job in October ^.^'
    elif month == 'november':
        challenge_text = 'Get a dev job in November ^.^'
    elif month == 'december':
        challenge_text = 'Get a dev job in December ^.^'
    else:
        return HttpResponseNotFound('Oops! This month is not supported!')
    return HttpResponse(challenge_text)






