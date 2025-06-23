from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class abexam(models.Model):
    exam_name = models.CharField(max_length=255, verbose_name='Название экзамена')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания записи')
    exam_date = models.DateField(verbose_name='Дата проведения экзамена')
    image = models.ImageField(upload_to='exam_images/', verbose_name='Изображение задания', blank=True, null=True)
    users = models.ManyToManyField(User, related_name='exams', verbose_name='Пользователи')
    is_public = models.BooleanField(default=False, verbose_name='Опубликовано')

    def __str__(self):
        return str(self.exam_name)
