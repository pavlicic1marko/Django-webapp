from django.urls import path
from users.views import RegisterView, LoginView, HomeView, LogoutView

urlpatterns = [
    path('register', view=RegisterView.as_view()),
    path('login', view=LoginView.as_view()),
    path('home', view=HomeView.as_view()),
    path('logout', view=LogoutView.as_view())
]