from django.urls import path,include
from .views import HomeView,GroupOrFriendsView,SignUpView,SignInView


urlpatterns = [
    path("", HomeView.as_view(),name="home"),
    path("signup/",SignUpView.as_view(),name='register'),
    path("signin/",SignInView.as_view(), name='login'),
    path("<str:category>/", GroupOrFriendsView.as_view()),
]