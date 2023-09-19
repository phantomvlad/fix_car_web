from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('allauth.urls')),
    path('account/', include('users.urls')),
    path('cars/', include('cars.urls')),
    path('', include('pages.urls'))
]
