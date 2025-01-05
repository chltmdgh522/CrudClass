from django.urls import path
from .views import *
from django.conf import settings
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

app_name = 'comment'

urlpatterns = [
    # 댓글 작성
    path('comment/<int:pk>/create', comment_create, name='comment_create'),

    # 댓글 삭제
    path('comment/<int:pk>', comment_delete, name='comment_delete'),



]
