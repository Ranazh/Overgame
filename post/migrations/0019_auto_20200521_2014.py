# Generated by Django 3.0.5 on 2020-05-21 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0018_auto_20200518_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='gameLink',
            field=models.CharField(default='add link', max_length=500),
        ),
    ]
