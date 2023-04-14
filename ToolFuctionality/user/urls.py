from django.conf import settings
from django.urls import path, include
from . import views
from user.views import Register
# from ToolFuctionality.user.views import Register

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('', views.openUser),
    path('register/', Register.as_view(), name='register'),
    # path('login', views.loginUser, name='login'),
    # path('registration', views.registerUser, name='register'),
    # path('tool', include('django.contrib.auth.urls')),
]
