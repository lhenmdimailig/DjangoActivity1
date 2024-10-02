from django.shortcuts import render

def services(request):
    return render(request, 'apptwo/services.html')
def portfolio(request):
    return render(request, 'apptwo/portfolio.html')
def testimonials(request):
    return render(request, 'apptwo/testimonials.html')
