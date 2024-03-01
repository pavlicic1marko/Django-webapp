from rest_framework.views import APIView
from .models import User
from .serializer import UserSerializer
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime


# Create your views here.
class RegisterView(APIView):
    def post(self, requests):
        serializer = UserSerializer(data=requests.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')  # TODO read secret from config fo not hardcode
        token.encode().decode('utf-8')

        response = Response()
        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }

        return response


class HomeView(APIView):
     def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated')

        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)

        return Response(serializer.data)


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message':'user is logged out'
        }

        return response


class UserByIdView(APIView):
    def get(self, request, id=id):
        user = User.objects.filter(id=id).first()
        serializer = UserSerializer(user)

        return Response(serializer.data)

    def delete(self, request, id=id):
        user = User.objects.filter(id=id).first()
        serializer = UserSerializer(user)
        user.delete()

        return Response(serializer.data)

    def patch(self, request, id=id):
        email = request.data['email']
        name = request.data['name']
        password = request.data['password']
        user = User.objects.filter(id=id).first()
        user.email = email
        user.name = name
        user.set_password(password)
        user.save()

        serializer = UserSerializer(user)
        return Response(serializer.data)





