"""A  User created file that is connects to Project Url"""

from django.urls import path
from django.views import generic

from . import views

urlpatterns = [

	path('', views.HomePageView.as_view(),name='home'),
]
