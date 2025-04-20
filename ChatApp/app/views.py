from django.shortcuts import render
from django.views.generic import TemplateView,ListView
# Create your views here.
from django.http import HttpResponse
from django.views.generic import CreateView
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView,LogoutView
from .forms import RegisterForm,LoginForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
import random


User = get_user_model()


class HomeView(LoginRequiredMixin,TemplateView):
    template_name = "mainChatapp.html"
    extra_context = {
        "category" : "friends"
    }

#channels/
class GroupOrFriendsView(LoginRequiredMixin,ListView):
    template_name = "leftbar/friendGroupsList.html"
    extra_context = {'load' : True}
    model = User
  
 
class SignUpView(CreateView):
    template_name = "authentication/Register.html"
    form_class = RegisterForm
    success_url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):

        if self.request.user.is_authenticated:
            return redirect('home')
        return super().get(request, *args, **kwargs)
        

#/showchat/<int:user_id>
class ChatWindowView(LoginRequiredMixin, TemplateView):
    template_name = 'rightbar/channelchatWindow.html' 

    def get_context_data(self, **kwargs):
        kwargs.setdefault("view", self)
        self.extra_context = { 'messages' : random.choice(["whatdfsd", "hi buddy whats up", "nice to meet ya"])}
        if self.extra_context is not None:
            kwargs.update(self.extra_context)
        return kwargs


class SignInView(LoginView):
    template_name = 'authentication/login.html'
    # form_class = LoginForm
    success_url = reverse_lazy('home')


class SignOutView(LogoutView):
    pass