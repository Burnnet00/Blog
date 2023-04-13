from django.db import models


class Post(models.Model):
    '''Data post'''
    title = models.CharField('Заголовок записи', max_length=100)
    description = models.TextField('Текст записи')
    autor = models.CharField('Имя автора', max_length=100)
    date = models.DateField('Дата публикации')
    image = models.ImageField('Изображения', upload_to='image/%Y')

    def __str__(self):
        return f'{self.title}, {self.autor}'

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
