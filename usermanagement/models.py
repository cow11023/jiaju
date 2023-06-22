from django.db import models



class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    # 添加其他用户属性，如密码、地址等

    def __str__(self):
        return self.name
# Create your models here.
