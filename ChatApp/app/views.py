from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
from django.http import HttpResponse


# def HomeView(request):
#     return render(request, "mainChatapp.html")

class HomeView(TemplateView):
    template_name = "mainChatapp.html"
    extra_context = {
        "category" : "friends"
    }

class GroupOrFriendsView(TemplateView):
    template_name = "usersGroups.html"
 
        