from django.urls import path
from . import views
from rest_framework.authtoken import views as register_view

urlpatterns = [
    path('test',views.home,name='home'),
    path('covid19',views.get_map_josn),
    path('register',register_view.obtain_auth_token),
    path('coordiantes',views.coordinates)
]
