from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

monthly_challenges = {
    "january": "Get a dev job.",
    "february": "Get a dev job.",
    "march": "Get a dev job.",
    "april": "Get a dev job.",
    "may": "Get a dev job.",
    "june": "Get a dev job.",
    "july": "Get a dev job.",
    "august": "Get a dev job.",
    "september": "Get a dev job.",
    "october": "Get a dev job.",
    "november": "Get a dev job.",
    "december": "Get a dev job.",
}


# Create your views here.

def month_challenge_by_number(request, month):
    return HttpResponse(month)


def month_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("Oops! Error 404")
