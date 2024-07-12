from django.shortcuts import render, redirect
from . import serializers
from rest_framework.views import APIView
from django.contrib.auth.tokens import  default_token_generator
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from rest_framework.response import Response
# from django.contrib.auth.models import User
from rest_framework import status
from django.http import HttpResponse
# Create your views here.
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate , login, logout
from rest_framework.authtoken.models import Token
from freelancer_platform.settings import LOGIN_URL
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import CustomUser


User = get_user_model()

class UserRegistrationAPIView(APIView):
    serializer_class = serializers.RegistrationSerialzers

    def post (self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            print(user.pk)
            confirm_link= f'http://127.0.0.1:8000/accounts/active/{uid}/{token}'
            name = f"Hello {user.first_name}"
            email_subject = "Verify Your Email Address - Complete Your Registration"
            email_body = render_to_string('./accounts/confirm_email.html',{'confirm_link':confirm_link, 'name':name})
            email = EmailMultiAlternatives(email_subject,'',to=[user.email])
            email.attach_alternative(email_body, 'text/html')
            email.send()
            return Response("Check your mail for confirmation")
        return Response(serializer.errors)


def activate(request, uid64, token):
    try:
        uid = urlsafe_base64_decode(uid64).decode() 
        user = User._default_manager.get(pk=uid)
        # print(user)
    except(User.DoesNotExist):
        user = None
        print('okay')
    
    if user is not None and default_token_generator.check_token(user,token):
        user.is_active = True
        user.save()
        return redirect(LOGIN_URL)
    else:
        return HttpResponse("Activation link is invalid!", status=status.HTTP_400_BAD_REQUEST)




def get_user_type_by_username(request, username):
    user = get_object_or_404(CustomUser, username=username)
    return JsonResponse({'user_type': user.user_type , 'user_id':user.id})

    


