# Generated by Django 2.1.5 on 2019-03-05 15:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('openbook_posts', '0017_post_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
