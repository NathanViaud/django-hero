# Generated by Django 4.1.5 on 2023-02-18 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='image',
            field=models.TextField(default='img/dragon.png'),
        ),
    ]