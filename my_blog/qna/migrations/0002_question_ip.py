# Generated by Django 4.0.2 on 2022-03-28 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qna', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='ip',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
