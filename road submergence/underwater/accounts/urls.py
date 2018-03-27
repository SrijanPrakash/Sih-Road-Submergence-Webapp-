from django.conf.urls import url,include
from django.contrib.auth import views as auth_views
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'accounts'
router=DefaultRouter()
router.register('profile',views.UserProfileViewset)
router.register('log',views.LoginViewSet,base_name='log')


urlpatterns = [
    url(r'login/$',
    auth_views.LoginView.as_view(template_name= 'accounts/login.html'),
     name='login'),
    url(r'logout/$',auth_views.LogoutView.as_view(),name='logout'),
    url(r'signup/$',views.SignUp.as_view(),name='signup'),
    url(r'',include(router.urls))


]
