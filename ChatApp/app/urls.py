from django.urls import path,include
from .views import HomeView,GroupOrFriendsView,SignUpView,SignInView,SignOutView,ChatWindowView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", HomeView.as_view(),name="home"),
    path("signup/",SignUpView.as_view(),name='register'),
    path("signin/",SignInView.as_view(redirect_authenticated_user=True), name='login'),
    path("logout/",SignOutView.as_view(), name='logout'),
    path("showChat/<int:user_id>/",ChatWindowView.as_view()),
    path("channels/", GroupOrFriendsView.as_view()),
]
