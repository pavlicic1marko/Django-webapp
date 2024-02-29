from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from users.views import RegisterView

urlpatterns = [
    path('register', view=RegisterView.as_view())
]