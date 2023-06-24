from django.urls import path
from . import views

app_name = 'usermanagement'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('update-profile/', views.update_userprofile, name='update_profile'),
    path('user-list/', views.user_list, name='user_list'),
]
