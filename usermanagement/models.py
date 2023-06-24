from django.contrib.auth.models import AbstractUser,Group
from django.db import models
class User(AbstractUser):
    PERMISSION_CHOICES = [
        ('owner', '房主'),
        ('guest', '客人'),
    ]
    username = models.CharField(max_length=100)
    password1 = models.CharField(max_length=8)
    password2 = models.CharField(max_length=8)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=200)
    avatar = models.ImageField(upload_to='avatars/') ## 头像字段
    permission = models.CharField(max_length=10, choices=PERMISSION_CHOICES)
    phone = models.CharField(max_length=11)
    # 添加 related_name 参数
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='custom_user_set',
        help_text='The permissions this user has.',
        related_query_name='user',
    )
    # 添加 groups 字段，并设置 related_name
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name='custom_user_set',
        related_query_name='user',
    )
    def __str__(self):
        return self.username

# Create your models here.
