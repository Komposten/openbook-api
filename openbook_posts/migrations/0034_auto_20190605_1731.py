# Generated by Django 2.2 on 2019-06-05 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openbook_posts', '0033_auto_20190523_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.CharField(max_length=5000, null=True, verbose_name='text'),
        ),
        migrations.AlterField(
            model_name='postcomment',
            name='text',
            field=models.TextField(max_length=560, verbose_name='text'),
        ),
    ]
