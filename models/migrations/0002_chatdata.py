# Generated by Django 4.2.4 on 2023-09-17 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='chatData',
            fields=[
               ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_email', models.CharField(max_length=100)),
                ('to_email', models.CharField(max_length=100)),
                ('to_message', models.CharField(max_length=10000)),
                ('from_message', models.CharField(max_length=10000)),
            ],
        ),
    ]
