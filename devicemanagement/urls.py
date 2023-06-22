from django.urls import path
from . import views

app_name = 'devices'

urlpatterns = [
    path('', views.device_list, name='device_list'),
    path('<int:device_id>/', views.device_detail, name='device_detail'),
    # 其他URL配置
]
