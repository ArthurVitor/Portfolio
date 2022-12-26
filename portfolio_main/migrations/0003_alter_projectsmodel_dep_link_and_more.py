# Generated by Django 4.1.4 on 2022-12-26 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_main', '0002_projectsmodel_dep_projectsmodel_dep_link_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectsmodel',
            name='dep_link',
            field=models.CharField(default='https://github.com/ArthurVitor', max_length=255, null=True, verbose_name='Link do deploy'),
        ),
        migrations.AlterField(
            model_name='projectsmodel',
            name='repo',
            field=models.CharField(default='https://github.com/ArthurVitor', max_length=255, null=True, verbose_name='Link do Repositorio'),
        ),
    ]