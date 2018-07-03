from django.urls import path

from . import views


app_name = 'apartments'
urlpatterns = [
    path('', views.ApartmentList.as_view(), name='list'),
    path('apartments/<int:pk>/detail/', views.ApartmentDetail.as_view(), name='detail'),
    path('apartments/new/', views.ApartmentCreate.as_view(), name='create'),
    path('apartments/<int:pk>/update/', views.ApartmentUpdate.as_view(), name='update'),
    path('apartments/<int:pk>/delete/', views.ApartmentDelete.as_view(), name='delete'),
]
