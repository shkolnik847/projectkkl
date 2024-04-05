from django.shortcuts import render
from .models import compHead

def index(request):
    context = compHead.objects.all()
    return render(request, 'base.html', {'context': context})