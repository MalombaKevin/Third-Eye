# Generated by Django 4.0.5 on 2022-06-22 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('third_eye_app', '0002_user_posts'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jirani',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jirani_name', models.CharField(max_length=200)),
                ('jirani_location', models.CharField(max_length=200)),
                ('jirani_population', models.CharField(max_length=100)),
            ],
        ),
    ]
