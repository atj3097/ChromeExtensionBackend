from django.shortcuts import render
from .models import Business
# Create your views here.
from django.http import HttpResponse
from django.template import loader


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def signup(request):
    if request.method == 'POST':
        if request.POST.get('Name') and request.POST.get('Location'):
            post = Business()
            post.name = request.POST.get('Name')
            post.location= request.POST.get('Location')
            post.save()

            return render(request, 'businesses/signup.html')

    else:
        return render(request, 'businesses/signup.html')
