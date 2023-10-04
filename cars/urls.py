from django.urls import path, include
from .views import CarPageView, CarPageNew, CarPageUpdate, CarPageList

urlpatterns = [
	path('<int:pk>', CarPageView.as_view(), name='car_show'),
	path('new/', CarPageNew.as_view(), name='car_create'),
	path('<int:pk>/update/', CarPageUpdate.as_view(), name='car_update'),
	path('<int:pk_car>/repairs/', include('repair.urls')),
	path('', CarPageList.as_view(), name='car_list')
]
