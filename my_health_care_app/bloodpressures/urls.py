from django.urls import path
from .views import bloodpressuer_list_view,bloodpressuer_create_view,bloodpressuer_detail_view,bloodpressure_update_view,bloodpressure_delete_view

app_name = 'bloodpressures'

urlpatterns = [
    path("list/",bloodpressuer_list_view,name="list"),
    path("add/",bloodpressuer_create_view,name="add"),
    path("detail/<int:pk>",bloodpressuer_detail_view,name="detail"),
    path("update/<int:pk>",bloodpressure_update_view,name="update"),
    path("delete/<int:pk>",bloodpressure_delete_view,name="delete"),
]
