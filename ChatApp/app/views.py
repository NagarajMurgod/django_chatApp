from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
from django.http import HttpResponse
from django.views.generic import CreateView
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from .forms import RegisterForm,LoginForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect

User = get_user_model()


class HomeView(LoginRequiredMixin,TemplateView):
    template_name = "mainChatapp.html"
    extra_context = {
        "category" : "friends"
    }

class GroupOrFriendsView(LoginRequiredMixin,TemplateView):
    template_name = "usersGroups.html"

 
class SignUpView(CreateView):
    template_name = "Register.html"
    form_class = RegisterForm
    success_url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
    
        if request.user.is_authenticated:
            return redirect('home')
        return super().get(request, *args, **kwargs)
                

class SignInView(LoginView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        """Handle GET requests: instantiate a blank version of the form."""
        if request.user.is_authenticated:
            return redirect('home')
        return self.render_to_response(self.get_context_data())