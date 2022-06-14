from django.db import models
# python manage.py startapp borad
# Create your models here.

class Board(models.Model):
    title = models.CharField('제목', max_length=255)
    countents = models.TextField('내용')





    