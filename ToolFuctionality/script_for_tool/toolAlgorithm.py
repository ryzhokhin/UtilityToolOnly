from django.http import HttpResponse


def view_on_web(request):

    userRequest = request

    budget = request.POST['budget']
    banks = []
    currency = request.POST['currency']

    for key, val in userRequest.POST.items():
        if key != 'csrfmiddlewaretoken' and key != 'budget' and key != 'currency':
            banks.append(val)

    userRequestCalc = {
        'budget': budget,
        'banks': banks,
        'currency': currency
    }
    return HttpResponse(userRequestCalc.items())


class Algorythm:
    def hello(request):
        print('Hello World')
