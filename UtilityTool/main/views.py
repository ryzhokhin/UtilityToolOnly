from django.shortcuts import render


# Create your views here.
def index(request):
    data = {
        'title': 'Main Page'
    }
    return render(request, 'main/index.html', data)


def tool(request):
    return render(request, 'main/tool.html')
