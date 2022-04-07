from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from .yasg import urlpatterns as swagger_urls
from aggregator.views import main_page

urlpatterns = [
    path("", main_page, name="main"),
    path('admin/', admin.site.urls),

    # api
    path('api/v1/', include('aggregator.api.v1.urls')),
]
urlpatterns += swagger_urls

admin.site.site_header = f"{settings.PROJECT_NAME}"
admin.site.site_title = f"Админ панель - {settings.PROJECT_NAME}"
admin.site.index_title = f"Добро пожаловать в {settings.PROJECT_NAME}"
