from django.urls import path

from taskapp import views

urlpatterns = [
    path('',views.home),
    path('signin',views.signin_fun,name='signin'),
    path('login',views.login_fun,name='login'),
    path('display/',views.display_fun,name='display'),

]