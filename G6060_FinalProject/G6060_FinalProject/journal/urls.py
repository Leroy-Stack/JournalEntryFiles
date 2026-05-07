from django.urls import path
from journal import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/', views.journal_api, name='journal_api'), # Lab 10 service
]