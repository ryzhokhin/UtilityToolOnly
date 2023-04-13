from django.shortcuts import render, redirect
from .forms import UserBaseForm
from .models import UserBase


# Create your views here.
def registration(request):
    error = ''
    if request.method == 'POST':
        form = UserBaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tool')
        else:
            error = 'Form input is incorrect'

    form = UserBaseForm()

    data = {
        'form': form,
        'error': error
    }
    # users = UserBase.objects.all()
    return render(request, 'usertool/registration.html', data )
