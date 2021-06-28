from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path("registration/", views.reg, name="registration"),
    path('registration/signUp', views.signUp, name="signUp"),
    path('logIn', views.logIn, name="logIn"),
    path('userDetails', views.logIn, name="logIn"),

]
