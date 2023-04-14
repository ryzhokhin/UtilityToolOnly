from django.shortcuts import render, redirect
from django. contrib.auth import login, authenticate
from django.views import View

from user.forms import UserCreationForm


# Create your views here.

# def loginUser(request):
#     return render(request, 'user/login.html')
#
# def userHome(request):
#     return render(request, 'user/user_home.html')
#
# def registerUser(request):
#     return render(request, 'user/registration.html')

class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, requset):
        form = UserCreationForm(requset.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(requset, user)
            return redirect('main')
        context = {
            'form': form
        }
        return render(requset, self.template_name, context)
