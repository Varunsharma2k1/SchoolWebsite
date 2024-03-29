# Generated by Django 4.2.1 on 2023-05-05 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chanakya', '0015_delete_registration_alter_career_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=10)),
                ('LastName', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('LastSchool', models.CharField(blank=True, max_length=30)),
                ('FatherName', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=10)),
                ('Address', models.CharField(max_length=50)),
                ('SiblingName', models.CharField(blank=True, max_length=20)),
                ('Class', models.CharField(blank=True, max_length=10)),
            ],
        ),
    ]
