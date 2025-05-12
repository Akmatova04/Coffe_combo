from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('menu.urls')), # menu тиркемесинин URL даректерин кошуу
]

# Иштеп чыгуу учурунда медиа файлдарды көрсөтүү үчүн
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # Эгер STATIC_ROOT аныкталса