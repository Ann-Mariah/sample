# Generated by Django 4.2.4 on 2023-09-13 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0005_student_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image/'),
        ),
    ]
