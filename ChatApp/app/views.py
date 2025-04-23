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
from django.shortcuts import get_object_or_404
from django.views import View
from .services import get_or_create_privateChat,get_chat_messages
from .models import Chats,Messages

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
class ChatHistoryView(LoginRequiredMixin, ListView):
    template_name = 'rightbar/channelchatWindow.html' 

    def get_queryset(self):
        group_id = self.kwargs.get('group_id')
        messages = get_chat_messages(group_id)
        return messages



class StartNewChatView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        other_user_id = kwargs.get('user_id')
        other_user = get_object_or_404(User, id=other_user_id)
        chat,created = get_or_create_privateChat(request.user, other_user)
        return redirect('listChatMessages',group_id=chat.group_id)



class SignInView(LoginView):
    template_name = 'authentication/login.html'
    # form_class = LoginForm
    success_url = reverse_lazy('home')


class SignOutView(LogoutView):
    pass

