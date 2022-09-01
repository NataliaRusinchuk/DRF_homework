from django.urls import path
from .views import *


urlpatterns = [
    path("product/list", ProductListView.as_view()),
    path("product/<int:pk>", ProductObject.as_view()),
    path("product/change/<int:pk>", ProductObjectChange.as_view()),
    path("product/delete/<int:pk>", ProductObjectDelete.as_view()),
    path("product/create", ProductCreate.as_view()),
    path("orders", OrderView.as_view())
]