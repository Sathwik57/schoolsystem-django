# Generated by Django 3.2.9 on 2021-12-01 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0008_auto_20211201_1818'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='gradedassignment',
            constraint=models.UniqueConstraint(fields=('student', 'assignment'), name='unique_test'),
        ),
    ]
