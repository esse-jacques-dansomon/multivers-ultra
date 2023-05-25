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

import skill
from address.views import CountryListView, CountryDetailView
from developer import views as developer_views
from skill.views import SkillListView, SkillDetailView, SkillCategoryDetails, SkillCategoryListView
from ultra import settings
from ultra.settings import BASE_DIR
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
    path('api/developers', developer_views.developer_list, name='developer_list'),
    path('api/developers/<int:pk>', developer_views.developer_detail, name='developer_detail'),
    path('api/languages', developer_views.language_list, name='language_list'),
    path('api/status', developer_views.status_list, name='status_list'),
    path('api/levels', developer_views.level_list, name='level_list'),
    path('api/countries', CountryListView.as_view(), name='country_list'),
    path('api/countries/<int:country_id>', CountryDetailView.as_view(), name='country_detail'),
    path('api/skills', SkillListView.as_view(), name='skill_list'),
    path('api/skills/<int:skill_id>', SkillDetailView.as_view(), name='skill_detail'),
    path('api/skill-categories', SkillCategoryListView.as_view(), name='skill_category_list'),
    path('api/skill-categories/<int:pk>', SkillCategoryDetails.as_view(), name='skill_category_list'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
