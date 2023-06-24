from django.shortcuts import render, get_object_or_404
from .models import Room

def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'room/room_list.html', {'rooms': rooms})

def room_temperature(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    device = room.device  # 获取房间关联的设备对象

    if device:
        temperature = device.temperature  # 获取设备的温度信息
        current_temperature = device.current_temperature  # 获取设备的当前温度信息
    else:
        temperature = None
        current_temperature = None

    context = {
        'room': room,
        'temperature': temperature,
        'current_temperature': current_temperature
    }

    return render(request, 'room/room_temperature.html', context)


# Create your views here.
