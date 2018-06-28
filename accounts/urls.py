from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views

app_name = 'accounts'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('tenant/signup/', views.TenantSignUpView.as_view(), name='tenant_signup'),
    path('landlord/signup/', views.LandLordSignUpView.as_view(), name='landlord_signup')
]