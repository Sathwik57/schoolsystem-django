# Generated by Django 3.2.9 on 2021-12-02 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0010_gradedassignment_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='gradedassignment',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='grades'),
        ),
    ]
