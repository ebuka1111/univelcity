from django.shortcuts import render
from rest_framework.response import Response
from .serializers import UserRegistrationSerializer
from rest_framework.views import APIView


# Create your views here.

class CreateUserView(APIView):
    def post(self, request, *args, **kwargs):
        new_data = UserRegistrationSerializer(data=request.data)
        new_data.is_valid(raise_exception=True)
        new_data.save()
        return Response({"Success": "Thanks for signing up"})