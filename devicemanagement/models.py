from django.db import models
from roommanagement.models import Room


class Device(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    parent_device = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    temperature = models.FloatField()  # 温度字段
    current_temperature = models.FloatField()  # 当前温度字段
    fan_speed = models.IntegerField()  # 风速字段
    current_fan_speed = models.IntegerField()  # 当前风速字段
    energy = models.FloatField(default=0)  # 能耗字段

    def update_statistics(self):
        # 更新统计数据
        self.total_devices = Device.objects.count()
        self.average_temperature = Device.objects.aggregate(models.Avg('temperature'))['temperature__avg']
        self.total_energy = Device.objects.aggregate(models.Sum('energy'))['energy__sum']
        self.save()

    def set_temperature(self, new_temperature):
        # 设置温度逻辑
        self.temperature = new_temperature
        # 执行其他相关操作

    def set_fan_speed(self, new_fan_speed):
        # 设置风速逻辑
        self.fan_speed = new_fan_speed
        # 执行其他相关操作

    def update_current_temperature(self, new_temperature):
        # 更新当前温度逻辑
        self.current_temperature = new_temperature
        # 执行其他相关操作

    def update_current_fan_speed(self, new_fan_speed):
        # 更新当前风速逻辑
        self.current_fan_speed = new_fan_speed
        # 执行其他相关操作

    def __str__(self):
        return self.name

    # 这里可以定义设备控制的方法、状态更新等其他逻辑
    def get_device_temperature(self):
        return self.temperature

    def get_device_current_temperature(self):
        return self.current_temperature
