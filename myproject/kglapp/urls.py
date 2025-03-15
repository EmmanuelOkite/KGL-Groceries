from django.urls import path
from . import views  # Ensure you're importing views correctly
from . views import *

urlpatterns = [
    path('', views.home, name='home'),  # Example path
]


from django.urls import path
from .views import landing_page

urlpatterns = [
    path('', landing_page, name='landing_page'), 
    path('branches',branches, name="branches"),
    path('base', base, name="base"),
    path('director', director, name="director"),
    path('manager', manager, name="manager"),
    path('attendant', attendant, name="attendant"),
    path('create/', views.create_produce, name='create_produce'),
    path('list/', views.produce_list, name='produce_list'),
]
