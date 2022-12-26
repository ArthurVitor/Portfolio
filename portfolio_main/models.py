from django.db import models

# Create your models here.
class ProjectsModel(models.Model):
    nm = models.CharField(max_length=255, null=False, verbose_name='Nome')
    img_url = models.CharField(max_length=255, null=False, verbose_name='Url da Imagem')
    tec_us = models.CharField(max_length=255, null=False, verbose_name='Tecnologias Usadas')
    desc = models.TextField(null=False, verbose_name='Descrição')
    repo = models.CharField(max_length=255, null=True, verbose_name='Link do Repositorio', default='https://github.com/ArthurVitor')
    dep = models.BooleanField(default=False, verbose_name='Foi feito deploy?')
    dep_link = models.CharField(max_length=255, null=True, default='https://github.com/ArthurVitor', verbose_name='Link do deploy')

    def __str__(self):
        return self.nm