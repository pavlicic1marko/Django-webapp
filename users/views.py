from rest_framework.views import APIView
from .models import User
from .serializer import UserSerializer
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed


# Create your views here.
class RegisterView(APIView):
    def post(self, requests):
        serializer = UserSerializer(data=requests.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class LoginView(APIView):
    def post(self,request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password')

        return Response({
            'message: success'
        })