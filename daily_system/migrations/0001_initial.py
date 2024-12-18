# Generated by Django 5.1.3 on 2024-11-27 20:46

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.IntegerField()),
                ('lesson_date', models.DateTimeField()),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('user', models.ManyToManyField(related_name='Grade', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
