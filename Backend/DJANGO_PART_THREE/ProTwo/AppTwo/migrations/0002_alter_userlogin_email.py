# Generated by Django 4.0.6 on 2022-11-13 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppTwo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlogin',
            name='email',
            field=models.EmailField(max_length=150, unique=True),
        ),
    ]
