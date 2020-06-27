from django.urls import path
from passwds import views

urlpatterns = [

    path('passwds/test/',views.test),
    path('',views.index,name='index'),
    
]