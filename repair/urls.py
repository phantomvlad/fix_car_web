from django.urls import path
from .views import *

app_name = 'repairs'

urlpatterns = [
    path('<int:pk_repair>/', RepairPageView.as_view(), name='show'),
    path('create/', RepairPageNew.as_view(), name='create')
]
