from django.urls import path

from .views import (
    glucose_detail_view,
    glucoses_create_view,
    glucoses_delete_view,
    glucoses_list_view,
    glucoses_update_view,
)

app_name = "glucoses"

urlpatterns = [
    path("", glucoses_list_view, name="list"),
    path("<int:pk>/", glucose_detail_view, name="detail"),
    path("add/", glucoses_create_view, name="add"),
    path("<int:pk>/update/", glucoses_update_view, name="update"),
    path("<int:pk>/delete/", glucoses_delete_view, name="delete"),
]
