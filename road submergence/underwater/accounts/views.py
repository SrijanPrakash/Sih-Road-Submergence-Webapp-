from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView,TemplateView
from . import forms
import requests
from .models import Rain
from graphos.renderers.gchart import LineChart
from rest_framework import viewsets
from . import serializers
from . import models


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


class UserProfileViewset(viewsets.ModelViewSet):

    serializer_class = serializers.UserProfileSerializer
    queryset= models.User.objects.all()
