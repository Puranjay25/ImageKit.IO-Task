# Generated by Django 2.2.3 on 2020-03-19 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200319_1612'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdetail',
            name='id',
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='email',
            field=models.EmailField(max_length=255, primary_key=True, serialize=False),
        ),
    ]