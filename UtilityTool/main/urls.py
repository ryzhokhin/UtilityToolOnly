from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('tool', views.tool, name='tool')
]