# Generated by Django 3.0.2 on 2020-01-21 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200117_2336'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='../static/img/default_post.jpg', upload_to='photos/'),
        ),
    ]
