from django.shortcuts import render, redirect
from django. contrib.auth import login, authenticate
from django.views import View
from django.http import HttpResponse
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
def openUser(request):
    return redirect('main')

def loginUser(request):
    return redirect('login')

def toolFormOperation(request):
    USER_CREATED_FORM = request
    return HttpResponse(USER_CREATED_FORM)
    # Zinli = request.POST['Zinli']
    # Wise = request.POST['Wise']
    # AdvCash = request.POST['AdvCash']
    # ABA = request.POST['ABA']
    # Zelle = request.POST['Zelle']
    # Utopia = request.POST['Utopia']
    # AirTM = request.POST['AirTM']
    # Perfect_Money = request.POST['Perfect_Money']
    # Payeer = request.POST['Payeer']
    # Skrill = request.POST['Skrill']
    # Monobank = request.POST['Monobank']
    # return HttpResponse("hello ✡️")

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
