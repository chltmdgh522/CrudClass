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

    # 글 자세히 보기
    path('detail/<int:pk>', board_detail, name='board_detail'),

    # 글 업데이트
    path('update/<int:pk>', board_update, name='board_update'),

    # 글 삭제
    path('delete/<int:pk>', board_delete, name='board_delete'),

]
