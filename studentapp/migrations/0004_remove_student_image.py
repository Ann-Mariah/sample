# Generated by Django 4.2.4 on 2023-09-13 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0003_student_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='image',
        ),
    ]
