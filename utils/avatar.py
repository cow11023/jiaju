import random

DEFAULT_AVATARS = [
    'avatars/avatar1.png',
    'avatars/avatar2.png',
    'avatars/avatar3.png',
    'avatars/avatar4.png',
    # 添加更多默认头像路径
]

def get_random_default_avatar():
    return random.choice(DEFAULT_AVATARS)

def handle_avatar_upload(avatar):
    # 处理用户上传的头像文件
    # 可以在这里实现保存、重命名等逻辑
    # 返回处理后的头像路径
    return 'avatars/user_uploads/' + avatar.name
