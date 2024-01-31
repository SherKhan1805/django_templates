from django.db import models


class Cards(models.Model):
    title = models.CharField(max_length=150, verbose_name='заголовок')
    content = models.TextField(verbose_name='Контент')
    image = models.ImageField(upload_to='material/', verbose_name='изображение')
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}. {self.content}.'

    class Meta:
        verbose_name = 'карта'
        verbose_name_plural = 'карты'
        ordering = ('title',)
