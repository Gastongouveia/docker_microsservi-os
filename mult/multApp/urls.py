from django.urls import path
from . import views

urlpatterns = [
    path('', views.mult, name='mult'),
]