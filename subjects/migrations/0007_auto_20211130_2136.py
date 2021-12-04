# Generated by Django 3.2.9 on 2021-11-30 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0006_auto_20211130_2120'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='options',
        ),
        migrations.AddField(
            model_name='question',
            name='option1',
            field=models.CharField(default='a', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='option2',
            field=models.CharField(default='a', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='option3',
            field=models.CharField(default='a', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='option4',
            field=models.CharField(default='a', max_length=100),
            preserve_default=False,
        ),
    ]
