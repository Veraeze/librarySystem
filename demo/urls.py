from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.greet),
    path('hello/<str:name>/', views.greet_me)
]