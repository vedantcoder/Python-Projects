# Generated by Django 2.2.13 on 2020-10-11 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0006_auto_20201011_1607'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Click link above to read the blog post...', max_length=255),
        ),
    ]
