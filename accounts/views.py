from django.shortcuts import render
from django.contrib.auth import get_user_model 
User = get_user_model()
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.status import(
    HTTP_400_BAD_REQUEST,
    HTTP_201_CREATED,
    HTTP_404_NOT_FOUND,
)
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
# from django.views.decorators.csrf import csrf_exempt
# from django.views.decorators.csrf import csrf_protect

# @csrf_protect
# @csrf_exempt
class SignupView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        data = self.request.data
        
        name = data['name']
        email = data['email']
        password = data['password']
        password2 = data['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                return Response({'error': 'email already exist'})
            else:
                if len(password) < 6:
                    return Response({'error': 'password must be at least 6 characters'})
                else:
                    user = User.objects.create_user(email=email, password=password, name=name)
                    user.save()
                    return Response({'success': 'User created successfully'})
        else:
            return Response({'error': 'password does not match'})
        
class SignInView(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request,format=None):
        
        email = request.data.get("email")
        password = request.data.get("password")
        # return Response({email, password}, HTTP_201_CREATED)
        if email is None or password is None:
            return Response({'error':'in'}, status=HTTP_400_BAD_REQUEST)
        if User.objects.filter(email=email, password=password).exists:
            # return Response({"User": User.objects.all()[0]}, 200)
        
            # return Response({'error':'user not found'}, status=HTTP_404_NOT_FOUND)
            token = Token.objects.get_or_create(User)
            return Response({'token':token.key}, status=HTTP_201_CREATED)