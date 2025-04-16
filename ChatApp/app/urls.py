from django.urls import path,include
from .views import HomeView,GroupOrFriendsView,SignUpView,SignInView,SignOutView,ChatWindowView


urlpatterns = [
    path("", HomeView.as_view(),name="home"),
    path("signup/",SignUpView.as_view(),name='register'),
    path("signin/",SignInView.as_view(redirect_authenticated_user=True), name='login'),
    path("logout/",SignOutView.as_view(), name='logout'),
    path("showChat/<int:user_id>/",ChatWindowView.as_view()),
    path("<str:category>/", GroupOrFriendsView.as_view()),
]