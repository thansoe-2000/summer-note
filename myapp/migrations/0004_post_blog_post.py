# Generated by Django 4.2.4 on 2023-08-17 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_remove_post_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='blog_post',
            field=models.TextField(blank=True, null=True),
        ),
    ]
