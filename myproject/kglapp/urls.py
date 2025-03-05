from django.urls import path
from . import views  # Ensure you're importing views correctly
from . views import *

urlpatterns = [
    path('', views.home, name='home'),  # Example path
]


from django.urls import path
from .views import landing_page

urlpatterns = [
    path('', landing_page, name='landing_page'),  # This sets the landing page as the homepage
]
