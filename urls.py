from django.urls import path
from .views import *

app_name = 'data'

urlpatterns = [
    
    path('', dataview, name='dataview'),
    
]