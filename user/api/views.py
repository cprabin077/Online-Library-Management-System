from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from django.contrib.auth import authenticate, login

from user.api.serializer import RegisterSerializer, LoginForm


class RegisterView(GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                    "message": "User successfully registered"
                },201)

        return Response(serializer.errors,400)


class LoginView(GenericAPIView):
    serializer_class = LoginForm

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return Response({
                        "message": "Login successful"
                    },200)
            
            else: 
                return Response({
                        "message": "Invalid username or password"
                    },401)
        else:
            return Response(serializer.errors,400)