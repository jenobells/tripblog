# Generated by Django 2.2.5 on 2019-09-19 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_blogimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image1',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='blog',
            name='image2',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='blog',
            name='image3',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.DeleteModel(
            name='BlogImage',
        ),
    ]
