# Generated by Django 2.1.3 on 2018-11-06 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20181107_0017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_title',
            field=models.CharField(max_length=200),
        ),
    ]
