# Generated by Django 4.2 on 2023-04-12 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usertool', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbase',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email'),
        ),
    ]
