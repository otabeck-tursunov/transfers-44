from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path('clubs/', views.clubs_view, name='clubs'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)