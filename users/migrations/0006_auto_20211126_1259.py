# Generated by Django 3.2.9 on 2021-11-26 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_user_is_superuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='address',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='contact_no',
            field=models.IntegerField(default=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='guardian',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='std',
            field=models.CharField(default='X', max_length=2),
            preserve_default=False,
        ),
    ]