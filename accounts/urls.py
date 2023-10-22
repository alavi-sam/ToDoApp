from django.urls import include, path
from .views import login


urlpatterns = [
    path('login/', login)
]
