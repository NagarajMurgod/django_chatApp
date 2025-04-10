from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
from django.http import HttpResponse


def HomeView(request):
    return render(request, "chatapp.html")

# class HomeView(TemplateView):
#     template_name = "chatapp.html"