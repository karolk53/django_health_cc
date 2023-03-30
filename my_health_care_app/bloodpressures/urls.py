from django.urls import path

from .views import (
    bloodpressuer_create_view,
    bloodpressuer_detail_view,
    bloodpressuer_list_view,
    bloodpressure_delete_view,
    bloodpressure_update_view,
)

app_name = "bloodpressures"

urlpatterns = [
    path("", bloodpressuer_list_view, name="list"),
    path("add/", bloodpressuer_create_view, name="add"),
    path("<int:pk>/", bloodpressuer_detail_view, name="detail"),
    path("<int:pk>/update/", bloodpressure_update_view, name="update"),
    path("<int:pk>/delete/", bloodpressure_delete_view, name="delete"),
]
