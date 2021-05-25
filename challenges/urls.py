from django.urls import path

#  URL file used for storing URL's for App

from . import views  # import from same file with '.'

urlpatterns = [
    path("<int:month>", views.month_challenge_by_number),  # Order matters
    path("<str:month>", views.month_challenge)  # Creates URLconf for views  /  accesses function and param in views.py
]
