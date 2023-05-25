from django.urls import path

from developer import views

urlpatterns = [
    path('developer', views.developer_list),
    path('<int:pk>', views.developer_detail),
    path('languages', views.language_list),
    path('status', views.status_list),
    path('levels', views.level_list),
]
