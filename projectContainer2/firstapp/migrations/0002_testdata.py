# Generated by Django 3.0.1 on 2020-03-13 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StudentName', models.CharField(max_length=50)),
                ('CourseName', models.CharField(max_length=20)),
                ('Email', models.EmailField(max_length=254)),
            ],
        ),
    ]