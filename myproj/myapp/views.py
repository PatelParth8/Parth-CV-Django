from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        query = Contact(name=name, email=email, message=message)
        query.save()
        return redirect(index)
    return redirect(index)