from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from .serializer import UserSerializer
from rest_framework.response import Response


# Create your views here.
class RegisterView(APIView):
    def post(self, requests):
        serializer = UserSerializer(data=requests.data)
        #serializer.is_valid(raise_exception=True)
        #serializer.save()
        #return Response(serializer.data)
        return Response('testttt')


