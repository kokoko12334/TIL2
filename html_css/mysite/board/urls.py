from django.urls import URLPattern, path

from . import views


#Routing

urlpatterns = [
    path('', views.index, name = 'index'),
    path('board', views.board_list, name = 'board_list'),
]





