# Generated by Django 4.2.2 on 2023-07-06 01:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dungeon', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dungeon',
            options={'ordering': ['-id'], 'verbose_name': '던전', 'verbose_name_plural': '던전'},
        ),
    ]