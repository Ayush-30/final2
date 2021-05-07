from django.urls import path

from . import views
from .views import *

# from .context_processors import notification_count


urlpatterns = [
    path('library/', library, name='library'),
    path('navbar/', library, name='navbar'),
    path('comp1/', library, name='comp1'),
path('error/', library, name='error'),


]
