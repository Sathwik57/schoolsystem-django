# Generated by Django 3.2.9 on 2021-11-28 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_teacher_contact_no'),
        ('subjects', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Subjects',
            new_name='Subject',
        ),
    ]