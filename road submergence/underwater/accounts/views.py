from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView,TemplateView
from . import forms
import requests
from .models import Rain
from graphos.renderers.gchart import LineChart
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from . import serializers
from . import models
from. import permissions


# Create your views here.
class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'


def rain(request):
    data_list = Rain.objects.all()
    data_dict = {'rain':data_list}
    return render(request,'test.html',context=data_dict)


class ThanksPage(TemplateView):
    template_name='thanks.html'

class HomePage(TemplateView):
    template_name = 'index.html'

class LoadPage(TemplateView):
    template_name='load.html'

class MailPage(TemplateView):
    template_name='mail.html'

class UserProfileViewset(viewsets.ModelViewSet):

    serializer_class = serializers.UserProfileSerializer
    queryset= models.User.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfiles,)

class LoginViewSet(viewsets.ViewSet):

    serializer_class=AuthTokenSerializer

    def create(self, request):

        return ObtainAuthToken().post(request)
