from django.shortcuts import render

def home(request):
    return render(request, 'appone/home.html')
def contact(request):
    return render(request, 'appone/contact.html')
def about(request):
    return render(request, 'appone/about.html')