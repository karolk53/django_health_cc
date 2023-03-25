from django.urls import path
from .views import glucoses_list_view,glucose_detail_view,glucoses_create_view,glucoses_delete_view,glucoses_update_view
from django.contrib.auth.views import TemplateView

app_name = 'glucoses'

urlpatterns = [
    path("list/",glucoses_list_view,name="list"),
    path("<int:pk>/",glucose_detail_view,name="detail"),
    path("add/",glucoses_create_view,name="add"),
    path("update/<int:pk>",glucoses_update_view,name="update"),
    path("delete/<int:pk>/",glucoses_delete_view,name="delete"),
]
