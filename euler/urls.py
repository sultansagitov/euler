from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('level/', include('courses.urls')),
    path('accounts/', include('accounts.urls')),
] 

urlpatterns += static("favicon.ico", document_root="assets/icon/favicon.ico") 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
