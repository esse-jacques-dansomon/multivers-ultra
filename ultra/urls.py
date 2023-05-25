"""
URL configuration for ultra project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import os
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_swagger.views import get_swagger_view

from developer import views
from ultra import settings
from ultra.settings import BASE_DIR
from django.conf.urls.static import static

MEDIA_ROOT = os.path.join(BASE_DIR, 'static/uploads ')
MEDIA_URL = '/static/uploads'
admin.site.site_header = "Ultra Admin"

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [

    # admin
    path("admin/", admin.site.urls),

    # auth
    path('api/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # rest api
    path('api/developers', views.developer_list, name='developer_list'),
    path('api/developers/<int:pk>', views.developer_detail, name='developer_detail'),
    path('api/languages', views.language_list, name='language_list'),
    path('api/status', views.status_list, name='status_list'),
    path('api/levels', views.level_list, name='level_list'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
