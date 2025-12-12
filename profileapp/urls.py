from django.urls import path
from .views import profileapp, add_new_service

app_name = "profileapp"
urlpatterns = [
    path('', profileapp, name="profileapp"),
    path('add', add_new_service, name="add_new_service"),
]
