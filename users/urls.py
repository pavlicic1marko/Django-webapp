from django.urls import path
from users.views import RegisterView, LoginView

urlpatterns = [
    path('register', view=RegisterView.as_view()),
    path('login', view=LoginView.as_view())

]