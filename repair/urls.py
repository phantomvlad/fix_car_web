from django.urls import path
from .views import *

urlpatterns = [
    path('<int:pk_repair>/', RepairPageView.as_view(), name='repair_show'),
    path('create/', RepairPageNew.as_view(), name='repair_create')
]
