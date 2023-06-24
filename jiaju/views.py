from django.shortcuts import render
from django.db.models import Avg, Sum
from devicemanagement.models import Device

def index(request):
    devices = Device.objects.all()
    total_devices = devices.count()
    average_temperature = devices.aggregate(Avg('temperature'))['temperature__avg']
    total_energy = devices.aggregate(Sum('energy'))['energy__sum']

    context = {
        'devices': devices,
        'total_devices': total_devices,
        'average_temperature': average_temperature,
        'total_energy': total_energy,
    }

    return render(request, 'index.html',context)