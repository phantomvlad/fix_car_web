from django.urls import path, include
from .views import CarPageView, CarPageNew, CarPageUpdate, CarPageList

app_name = 'cars'
urlpatterns = [
	path('<int:pk>', CarPageView.as_view(), name='show'),
	path('new/', CarPageNew.as_view(), name='create'),
	path('<int:pk>/update/', CarPageUpdate.as_view(), name='update'),
	path('<int:pk_car>/repairs/', include('repair.urls'), name='repairs'),
	path('', CarPageList.as_view(), name='list')
]
