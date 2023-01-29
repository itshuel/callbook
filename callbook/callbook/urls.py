from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views, settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.indexpage),
    path('login/', views.login),
    path('users/', include('users.urls'))
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
