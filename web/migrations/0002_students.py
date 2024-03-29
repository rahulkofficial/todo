# Generated by Django 4.2.4 on 2023-08-12 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=225)),
                ('last_name', models.CharField(max_length=225)),
                ('st_class', models.IntegerField()),
                ('division', models.CharField(max_length=1)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField()),
            ],
            options={
                'verbose_name_plural': 'students',
                'db_table': 'web_students',
            },
        ),
    ]
