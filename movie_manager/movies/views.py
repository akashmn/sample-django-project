from django.shortcuts import render

def create(request):
    return render(request, 'create.html')

def edit(request):
    return render(request, 'edit.html')

def list(request):
    return render(request, 'list.html')

# Create your views here.