from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import Group, Permission
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from utils.avatar import get_random_default_avatar
from .models import User


def register(request):
    if request.method == 'POST':
        try:
            username = request.POST['username']  # 用户名
            password1 = request.POST['password1']  # 密码
            password2 = request.POST['password2']  # 确认密码
            email = request.POST['email']  # 邮箱
            address = request.POST['address']  # 地址
            avatar = request.FILES.get('avatar')  # 头像
            phone = request.POST['phone']  # 手机号

            if password1 != password2:
                raise Exception('两次输入的密码不一致')

            # 检查是否已存在相同用户名的用户
            if User.objects.filter(username=username).exists():
                raise Exception('该用户名已被占用')

            # 创建一个具有客人权限的新用户
            user = User.objects.create_user(username=username, password=password1, email=email, address=address,
                                            phone=phone, permission='guest')

            if avatar:
                user.avatar = avatar
            else:
                # 如果未提供头像，则使用随机选择的默认头像
                user.avatar = get_random_default_avatar()

            user.save()

            # 登录新注册的用户
            user = authenticate(request, username=username, password=password1)
            login(request, user)

            return redirect('user_profile')

        except Exception as e:
            return render(request, 'users/register.html', {'error': str(e)})

    return render(request, 'users/register.html')


@login_required
def update_userprofile(request):
    user = request.user

    if request.method == 'POST':
        try:
            address = request.POST['address']  # 地址
            phone = request.POST['phone']  # 手机号
            avatar = request.FILES.get('avatar')  # 头像

            user.address = address
            user.phone = phone

            if avatar:
                user.avatar = avatar

            user.save()
            return redirect('user_profile')

        except Exception as e:
            return render(request, 'users/update_profile.html', {'user': user, 'error': str(e)})

    return render(request, 'users/update_profile.html', {'user': user})


@user_passes_test(lambda user: user.is_superuser)
def user_list(request):
    try:
        users = User.objects.all()
        return render(request, 'users/user_list.html', {'users': users})

    except Exception as e:
        return HttpResponse('发生错误：' + str(e), status=500)
