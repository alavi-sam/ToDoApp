from django.shortcuts import render
from django.views.generic import FormView


# Create your views here.


def login(request):
    if request.method == 'GET':
        return render(request, 'accounts-login.html')
