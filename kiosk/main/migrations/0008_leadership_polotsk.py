# Generated by Django 3.2.3 on 2021-05-28 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_workandmeeting'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leadership_Polotsk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('Leadership_Polotsk_photo', models.FileField(upload_to='Leadership_Polotsk/')),
                ('times', models.DateField()),
            ],
        ),
    ]
