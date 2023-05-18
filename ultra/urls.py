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
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from ultra import settings
from ultra.settings import BASE_DIR
from developer.views import DeveloperCreateView
from skill.views import SkillCreateView
from django.conf.urls.static import static

MEDIA_ROOT = os.path.join(BASE_DIR, 'static/uploads ')
MEDIA_URL = '/static/uploads'
admin.site.site_header = "Ultra Admin"
urlpatterns = [
                  # admin
                  path("admin/", admin.site.urls),

                  # auth
                  path('api/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
                  path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

                  # rest api
                  path("api/rest/skills/", SkillCreateView.as_view(), name='skills'),
                  path('api/rest/developers/', DeveloperCreateView.as_view(), name='developers'),
              ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
