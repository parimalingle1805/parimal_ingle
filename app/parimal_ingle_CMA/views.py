from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {})

def about(request):
    return render(request, 'about.html', {})

def addContact(request):
    return render(request, 'addContact.html', {})

def details(request):
    return render(request, 'details.html', {})