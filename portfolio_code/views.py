from django.shortcuts import render
from django.http import HttpResponse
from .models import project

# Create your views here.


def Home(request):

    proj = project.objects.all()
    context = {'proj': proj}
    return render(request, 'portfolio_code/Home.html', context)
