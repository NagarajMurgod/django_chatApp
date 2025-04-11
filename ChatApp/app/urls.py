from django.urls import path,include
from .views import HomeView,GroupOrFriendsView


urlpatterns = [
    path("", HomeView.as_view()),
    path("<str:category>/", GroupOrFriendsView.as_view())
]