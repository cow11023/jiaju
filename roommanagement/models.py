from django.db import models
class Room(models.Model):
    name = models.CharField(max_length=100)
    is_air_conditioner_on = models.BooleanField(default=False)  # 空调开关属性
    current_temperature = models.DecimalField(max_digits=5, decimal_places=2)
    current_fan_speed = models.CharField(max_length=50)
    # 其他空调相关字段
    def __str__(self):
        return self.name
# Create your models here.
