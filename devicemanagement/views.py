from django.shortcuts import render, get_object_or_404
from .models import Device

def device_list(request):
    devices = Device.objects.all()
    context = {'devices': devices}
    return render(request, 'devices/device_list.html', context)

def device_detail(request, device_id):
    device = get_object_or_404(Device, id=device_id)
    context = {'device': device}
    return render(request, 'devices/device_detail.html', context)

# 其他视图函数
