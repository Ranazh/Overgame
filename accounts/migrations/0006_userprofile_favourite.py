# Generated by Django 3.0.5 on 2020-05-22 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0021_auto_20200522_1836'),
        ('accounts', '0005_auto_20200426_1506'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='favourite',
            field=models.ManyToManyField(blank=True, null=True, related_name='favourite_post', to='post.Post'),
        ),
    ]
