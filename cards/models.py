from django.db import models

class Category(models.Model):
    name = models.CharField('Название категории', max_length=50)
    icon = models.ImageField('Иконка', upload_to='category/icon')
    icon_mobile = models.ImageField('Иконка', upload_to='category/icon_mobile')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'