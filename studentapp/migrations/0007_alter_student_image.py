# Generated by Django 4.2.4 on 2023-09-20 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0006_alter_student_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.ImageField(blank=True, default='static/images/icon2.png', null=True, upload_to='image/'),
        ),
    ]