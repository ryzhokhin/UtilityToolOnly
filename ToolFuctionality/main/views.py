from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def main_page(request):
    return render(request, 'main/main.html')

def main_page_design(request):
    return render(request, 'main/main-design.html')

