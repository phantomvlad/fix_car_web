from django.urls import path
from .views import UserPageView

urlpatterns=[
    path('<int:pk>/', UserPageView.as_view(), name='account_index'),
]
