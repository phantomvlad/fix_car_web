from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.defaults import page_not_found

urlpatterns = [
    path('admin/', admin.site.urls),
   # path('accounts/email/', page_not_found, {'exception': Exception('Not Found')}, name='account_email'),
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('users.urls')),
    path('cars/', include('cars.urls')),
    path('', include('pages.urls'))
]

if settings.DEBUG:
    urlpatterns += [path('__debug__/', include('debug_toolbar.urls'))] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)