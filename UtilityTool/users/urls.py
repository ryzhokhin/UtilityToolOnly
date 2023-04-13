from django.urls import path, include
from . import views
# from users.views import Register
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', views.Register.as_view(), name='registerNewUser')
]
