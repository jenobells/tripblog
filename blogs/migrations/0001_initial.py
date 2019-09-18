# Generated by Django 2.2.5 on 2019-09-18 07:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, null=True)),
                ('description', models.TextField(null=True)),
                ('date', models.TextField(null=True)),
                ('headerImage', models.ImageField(null=True, upload_to='images/')),
                ('location', models.CharField(max_length=40, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('posted_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]