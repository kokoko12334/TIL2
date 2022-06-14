from django.http import HttpResponse
from django.shortcuts import render
from .models import Board
# Create your views here.


#controller 응답 -> 요청 함수
def index(request):
    # return HttpResponse("Hello, world. you're at the polls index.")
    user_list = ['윤수','민표','수지']
    
    role = 'superuser'

    return render(request, 'index.html', {'name':'민표', 'user_list':user_list, 'role':role})   #html띄우기



def board_list(request):
    board_list = Board.objects.all()

    return render(request, 'board_list.html', {'board_list':board_list})


def board_write(request):
    return render(request, 'board_write.html')




