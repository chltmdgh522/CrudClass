from django.urls import path
from .views import *
from django.conf import settings
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

app_name = 'board'

urlpatterns = [

    # 글 쓰기
    path('create', board_create, name='board_create'),

    # 글 목록
    path('list', board_list, name='board_list'),

]
