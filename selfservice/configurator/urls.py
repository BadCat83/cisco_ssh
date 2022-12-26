from django.urls import path
from .views import *

urlpatterns = [
    #path('', ConfiguratorView.as_view(), name='home'),
    path('', test, name='test'),
]