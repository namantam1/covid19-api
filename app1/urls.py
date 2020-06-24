from django.urls import path
from . import views

urlpatterns = [
    path('test',views.home,name='home'),
    path('covid19',views.get_map_josn),
]
