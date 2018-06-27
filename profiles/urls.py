from django.urls import path


from . import views


app_name = 'profiles'
urlpatterns = [
    path('edit/', views.edit_profile, name='edit'),
    path('detail/<int:pk>/', views.UserDetail.as_view(), name='detail'),
]
