from django.db import models
from roommanagement.models import Room
from devicemanagement.models import Device

class Device(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    temperature = models.FloatField()  # 温度字段
    current_temperature = models.FloatField()  # 当前温度字段
    fan_speed = models.IntegerField()  # 风速字段
    current_fan_speed = models.IntegerField()  # 当前风速字段

    # 添加其他设备属性和方法

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
