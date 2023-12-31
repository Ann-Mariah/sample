# Generated by Django 4.2.4 on 2023-09-12 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_fname', models.CharField(max_length=100, null=True)),
                ('student_lname', models.CharField(max_length=100, null=True)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=10, null=True)),
                ('qualification', models.CharField(max_length=100, null=True)),
                ('image', models.ImageField(null=True, upload_to='image/')),
            ],
        ),
    ]
