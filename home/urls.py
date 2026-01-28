from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('onetimeride/', views.onetimeride, name='onetimeride'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),

]