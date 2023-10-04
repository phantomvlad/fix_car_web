from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('users.urls')),
    path('cars/', include('cars.urls')),
    path('', include('pages.urls'))
]
