from django.conf import settings
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main_page_design, name='main-design'),
    path('tool', views.main_page, name='main')

]