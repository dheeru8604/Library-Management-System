from django.urls import path
from Student.views import *


urlpatterns = [
    path('',home,name='home')
]
