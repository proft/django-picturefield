===================
django-picturefield
===================

Расширение ImageField с поддержкой кирилицы в именах файлов и ограничений на размер изображения по ширине и длине.

Установка
=========

1. Установка модуля и зависимостей `pip install 'git+https://github.com/proft/django-picturefield.git'`;

2. Пример использования:

::

    from django.db import models
    from picturefield.fields import PictureField


    class Animal(models.Model):
        title = models.CharField("Title", max_length=50)
        photo = PictureField("Photo", upload_to='animals', blank=True, null=True)

        class Meta:
            verbose_name = 'Animal'
            verbose_name_plural = 'Animals'

        def __unicode__(self):
            return self.title
