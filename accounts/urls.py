from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views

app_name = 'accounts'
urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', views.TenantSignUpView.as_view(), name='signup'),
]