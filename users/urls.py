from django.urls import path
from .views import UserPageView

urlpatterns = [
    path('<slug:slug_username>', UserPageView.as_view(), name='account_show'),
]
