# Generated by Django 4.1.4 on 2022-12-24 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectsmodel',
            name='dep',
            field=models.BooleanField(default=False, verbose_name='Foi feito deploy?'),
        ),
        migrations.AddField(
            model_name='projectsmodel',
            name='dep_link',
            field=models.CharField(default='https://atuar.io/', max_length=255, null=True, verbose_name='Link do deploy'),
        ),
        migrations.AddField(
            model_name='projectsmodel',
            name='repo',
            field=models.CharField(default='nulo', max_length=255, verbose_name='Link do Repositorio'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projectsmodel',
            name='tec_us',
            field=models.CharField(default='nulo', max_length=255, verbose_name='Tecnologias Usadas'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='projectsmodel',
            name='desc',
            field=models.TextField(verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='projectsmodel',
            name='img_url',
            field=models.CharField(max_length=255, verbose_name='Url da Imagem'),
        ),
        migrations.AlterField(
            model_name='projectsmodel',
            name='nm',
            field=models.CharField(max_length=255, verbose_name='Nome'),
        ),
    ]
