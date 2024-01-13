from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk fir at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day",
    'april': None,
    "may": None,
    "june": None,
    "july": None,
    "august": None,
    "september": None,
    "october": None,
    "november": None,
    "December": None
}


def index(request):
    months = []
    for i in monthly_challenges.keys():
        url = reverse("month-challenge", args=[i])
        months.append({'name': i, 'url': url})

    return render(request, 'challenges/index.html', {"months": months})


def monthly_challenge_by_number(request, month):
    forward_month = list(monthly_challenges.keys())[month]
    return HttpResponseRedirect(reverse("month-challenge", args=[forward_month]))


def monthly_challenge(request, month):
    if month in monthly_challenges.keys():
        return render(request, "challenges/challenge.html",
                      {"text": monthly_challenges[month], 'month': month.capitalize()})
    else:
        return HttpResponse("Wrong input")
