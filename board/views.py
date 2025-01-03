from django.shortcuts import render
def board_create(request):
    return render(request, 'board/create.html')


def board_list(request):
    return render(request, 'board/list.html')