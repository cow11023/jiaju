from django.urls import re_path
from devicemanagement.views import create_device, update_device, delete_device

app_name = 'devicemanagement'
urlpatterns = [
    # 其他URL配置...
    re_path(r'^devices/create/(?P<room_id>\d+)/$', create_device, name='create_device'),
    re_path(r'^devices/update/(?P<device_id>\d+)/$', update_device, name='update_device'),
    re_path(r'^devices/delete/(?P<device_id>\d+)/$', delete_device, name='delete_device'),
]