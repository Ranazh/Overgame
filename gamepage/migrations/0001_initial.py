# Generated by Django 3.0.5 on 2020-04-26 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0005_auto_20200426_1506'),
    ]

    operations = [
        migrations.CreateModel(
            name='GamePage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gameTitle', models.CharField(max_length=255)),
                ('text', models.TextField()),
                ('date_created', models.DateField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.UserProfile')),
            ],
        ),
    ]
