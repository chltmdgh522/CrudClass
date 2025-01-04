from django.shortcuts import render
from .models import Board
from comment.models import Comment
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse


def board_create(request):
    if request.method == 'POST':
        board = Board.objects.create(
            title=request.POST['title'],
            content=request.POST['content'],
        )
        return redirect(reverse('board:board_detail', args=[board.pk]))
    return render(request, 'board/create.html')


def board_list(request):
    boards = Board.objects.all()
    context = {'boards': boards}
    return render(request, 'board/list.html', context)


def board_detail(request, pk):
    boards = Board.objects.get(id=pk)
    comments = Comment.objects.filter(board=boards)
    context = {'board': boards
        , 'comment': comments}
    return render(request, 'board/read.html', context)


def board_update(request, pk):
    board = Board.objects.get(id=pk)
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        board.title = title
        board.content = content
        board.save()  # 변경사항 저장
        return redirect('board:board_detail', pk=board.pk)

    context = {'board': board}
    return render(request, 'board/update.html', context)


def board_delete(request, pk):
    if request.method == 'POST':
        board = Board.objects.get(id=pk)
        board.delete()
        return redirect('board:board_list')
    return redirect('home:main')
