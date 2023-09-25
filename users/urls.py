from django.urls import path
from .views import UserPageView

urlpatterns = [
    path('<slug:slug>', UserPageView.as_view(), name='account_show'),
]
