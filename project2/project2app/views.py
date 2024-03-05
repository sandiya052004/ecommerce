from django.shortcuts import render, HttpResponse, redirect
from .forms import SubscriptionForm
from django.http import HttpResponse
# Create your views here.
def index2(request):
    return render(request,'index.html')
def index11(request):
    return render(request,'html2.html')


def index(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Thank you for subscribing!')
    else:
        form = SubscriptionForm()
    return render(request, 'index.html', {'form': form})
    
    