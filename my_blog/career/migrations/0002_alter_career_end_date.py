# Generated by Django 4.2.2 on 2023-07-01 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='career',
            name='end_date',
            field=models.DateField(blank=True, null=True, verbose_name='종료날짜'),
        ),
    ]
