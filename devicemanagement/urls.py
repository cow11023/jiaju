from django.urls import re_path
from devicemanagement.views import create, update, delete

urlpatterns = [
    # 其他URL配置...
    re_path(r'^devices/create/(?P<room_id>\d+)/$', create, name='create_device'),
    re_path(r'^devices/update/(?P<device_id>\d+)/$', update, name='update_device'),
    re_path(r'^devices/delete/(?P<device_id>\d+)/$', delete, name='delete_device'),
]
