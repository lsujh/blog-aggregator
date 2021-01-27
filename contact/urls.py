from django.urls import path
from . import views

app_name = "contact"

urlpatterns = [
    path("", views.ContactCreate.as_view(), name="contact_create"),
]
