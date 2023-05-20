from django.db import models


class Post(models.Model):
    '''Data post'''
    title = models.CharField('Заголовок записи', max_length=100)
    description = models.TextField('Текст записи')
    autor = models.CharField('Имя автора', max_length=100)
    date = models.DateField('Дата публикации')
    img = models.ImageField('Изображения', upload_to='image/%Y')

    def __str__(self):
        return f'{self.title}, {self.autor}'

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'

class Comments(models.Model):
    """Comentariy"""
    email = models.EmailField()
    name = models.CharField('Имя',max_length=50)
    text_comments = models.TextField('Текст комментария', max_length=2000)
    post = models.ForeignKey(Post, verbose_name='Публикация', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}, {self.post}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

class Likes(models.Model):
    """Likes"""
    ip = models.CharField('', max_length=50)
    pos = models.ForeignKey(Post, verbose_name='Публикация', on_delete=models.CASCADE)
