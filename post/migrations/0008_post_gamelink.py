# Generated by Django 3.0.5 on 2020-05-17 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_remove_post_gamelink'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='gameLink',
            field=models.TextField(default='default value'),
        ),
    ]
