from django.urls import path
from . import views

urlpatterns = [
    path('', views.services, name='services'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('testimonials/', views.testimonials, name='testimonials'),
]
