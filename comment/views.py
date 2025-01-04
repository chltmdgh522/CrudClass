from django.shortcuts import render
from .models import Comment
from .models import Board
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse


def comment_create(request, pk):
    if request.method == 'POST':
        boards = Board.objects.get(id=pk)
        Comment.objects.create(
            board=boards,
            content=request.POST['content']
        )
        return redirect('board:board_detail', pk=boards.id)


def comment_delete(request, pk):
    if request.method == 'POST':
        comment = Comment.objects.get(id=pk)
        board_pk = comment.board.id
        comment.delete()
        return redirect('board:board_detail', pk=board_pk)
