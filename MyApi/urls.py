from django.urls import path
from . import views
from rest_framework.authtoken import views as register_view

urlpatterns = [
    path('covid19',views.get_map_josn),
    path('get_token',register_view.obtain_auth_token)
]