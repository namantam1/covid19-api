from django.urls import path,reverse_lazy
from .views import RegisterView,home,features,DeleteKey,AddKey
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic import CreateView
from .views import Token


urlpatterns = [
    path('register',RegisterView.as_view(),name='register'),
    path('login',LoginView.as_view(),name='login'),
    path('logout',LogoutView.as_view(),name='logout'),
    path('features',features,name='features'),
    path('',home,name='home'),
    path('<pk>/delete',DeleteKey.as_view(),name='delete'),
    path('addkey',AddKey.as_view(),name='addkey')
]
