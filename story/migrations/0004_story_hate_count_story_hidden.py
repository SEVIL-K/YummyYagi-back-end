# Generated by Django 4.2.7 on 2023-11-08 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0003_story_created_at_alter_content_story_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='hate_count',
            field=models.PositiveIntegerField(default=0, verbose_name='싫어요 개수'),
        ),
        migrations.AddField(
            model_name='story',
            name='hidden',
            field=models.BooleanField(default=False, verbose_name='숨김 여부'),
        ),
    ]