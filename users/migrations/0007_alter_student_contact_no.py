# Generated by Django 3.2.9 on 2021-11-26 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20211126_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='contact_no',
            field=models.IntegerField(null=True),
        ),
    ]