# Generated by Django 2.1.2 on 2018-10-20 13:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import openbook_common.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=560, verbose_name='text')),
                ('created', models.DateTimeField(editable=False)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PostComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(editable=False)),
                ('text', models.CharField(max_length=280, verbose_name='text')),
                ('commenter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts_comments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='image')),
                ('post', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='post', to='openbook_posts.Post')),
            ],
        ),
        migrations.CreateModel(
            name='PostReaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(editable=False)),
                ('reactor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reactions', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PostReactionEmoji',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='name')),
                ('shortcut', models.CharField(max_length=16, verbose_name='shortcut')),
                ('color', models.CharField(max_length=7, validators=[openbook_common.validators.hex_color_validator], verbose_name='color')),
                ('image', models.ImageField(upload_to='', verbose_name='image')),
                ('created', models.DateTimeField(editable=False)),
            ],
        ),
    ]
