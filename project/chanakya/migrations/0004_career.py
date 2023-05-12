# Generated by Django 4.2.1 on 2023-05-05 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chanakya', '0003_achievement_event_sport'),
    ]

    operations = [
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.TextField(max_length=10)),
                ('resume', models.FileField(max_length=254, upload_to='files/')),
                ('post', models.CharField(choices=[('prt', 'PRT'), ('tgt', 'TGT'), ('other', 'OTHER')], default='SELECT', max_length=20)),
            ],
        ),
    ]
