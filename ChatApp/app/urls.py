from django.urls import path,include
from .views import HomeView,GroupOrFriendsView,SignUpView,SignInView,SignOutView,ChatHistoryView,StartNewChatView, user_status_dot
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", HomeView.as_view(),name="home"),
    path("signup/",SignUpView.as_view(),name='register'),
    path("signin/",SignInView.as_view(redirect_authenticated_user=True), name='login'),
    path("logout/",SignOutView.as_view(), name='logout'),
    path("newchat/<int:user_id>/",StartNewChatView.as_view()),
    path("showchat/<str:group_id>/",ChatHistoryView.as_view(),name = 'listChatMessages'),
    path("user_status/<int:id>/",user_status_dot, name='user_status'),
    path("channels/", GroupOrFriendsView.as_view()),
]
