# Generated by Django 3.2.7 on 2021-10-23 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='Freaking awesome', max_length=255),
        ),
    ]
