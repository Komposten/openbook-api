# Generated by Django 2.2 on 2019-06-06 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openbook_auth', '0039_auto_20190605_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='bio',
            field=models.TextField(max_length=1000, null=True, verbose_name='bio'),
        ),
    ]