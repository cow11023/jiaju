from django.shortcuts import render, get_object_or_404, redirect
from broadlink import gendevice
from broadlink.exceptions import BroadlinkException
from .models import Room, Device

class DeviceManagementView:
    def create_device(self, request, room_id):
        room = get_object_or_404(Room, id=room_id)

        if request.method == 'POST':
            name = request.POST.get('name')
            temperature = request.POST.get('temperature')
            current_temperature = request.POST.get('current_temperature')
            fan_speed = request.POST.get('fan_speed')
            current_fan_speed = request.POST.get('current_fan_speed')

            try:
                # 使用 Broadlink Python SDK 创建设备
                device = gendevice()  # 请根据实际情况选择合适的函数来创建设备
                # 进行设备相关操作

                room.create_device(name, temperature, current_temperature, fan_speed, current_fan_speed)

                return redirect('room_temperature', room_id=room.id)

            except BroadlinkException as e:
                # 处理连接和通信异常
                error_message = str(e)
                context = {
                    'room': room,
                    'error_message': error_message,
                }
                return render(request, 'devices/create_device.html', context)

        context = {
            'room': room,
        }

        return render(request, 'devices/create_device.html', context)


    def update_device(self, request, device_id):
        device = get_object_or_404(Device, id=device_id)
        room = device.room

        if request.method == 'POST':
            device.name = request.POST.get('name')
            device.temperature = request.POST.get('temperature')
            device.current_temperature = request.POST.get('current_temperature')
            device.fan_speed = request.POST.get('fan_speed')
            device.current_fan_speed = request.POST.get('current_fan_speed')
            device.save()

            return redirect('room_temperature', room_id=room.id)

        context = {
            'room': room,
            'device': device,
        }

        return render(request, 'devices/update_device.html', context)


    def delete_device(self, request, device_id):
        device = get_object_or_404(Device, id=device_id)
        room = device.room

        if request.method == 'POST' and request.POST.get('_method') == 'DELETE':
            device.delete()
            room.update_statistics()
            return redirect('room_temperature', room_id=room.id)

        context = {
            'room': room,
            'device': device,
        }

        return render(request, 'devices/delete_device.html', context)

    def device_list(self, request):
        # 获取所有设备对象
        devices = Device.objects.all()

        context = {
            'devices': devices,
        }

        return render(request, 'devices/device_list.html', context)

device_management_view = DeviceManagementView()

def create_device(request, room_id):
    return device_management_view.create_device(request, room_id)

def update_device(request, device_id):
    return device_management_view.update_device(request, device_id)

def delete_device(request, device_id):
    return device_management_view.delete_device(request, device_id)
