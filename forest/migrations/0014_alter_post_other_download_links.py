# Generated by Django 3.2.1 on 2021-07-17 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forest', '0013_post_other_download_links'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='other_download_links',
            field=models.TextField(default=' {"not avalable":"https://"}'),
        ),
    ]