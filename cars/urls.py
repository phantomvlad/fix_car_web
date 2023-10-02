from django.urls import path, include
from .views import CarPageView, CarPageNew

urlpatterns = [
	path('<int:pk>', CarPageView.as_view(), name='car_show'),
	path('new/', CarPageNew.as_view(), name='car_create'),
	path('<int:pk_car>/repairs/', include('repair.urls'))
]
