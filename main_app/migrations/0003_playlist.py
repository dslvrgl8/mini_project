# Generated by Django 4.2.2 on 2023-07-01 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_character'),
    ]

    operations = [
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('characters', models.ManyToManyField(to='main_app.character')),
            ],
        ),
    ]
