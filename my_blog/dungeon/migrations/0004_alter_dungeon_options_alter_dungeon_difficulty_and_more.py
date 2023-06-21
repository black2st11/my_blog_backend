# Generated by Django 4.2.2 on 2023-06-21 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('me', '0004_alter_archiving_options_alter_education_options_and_more'),
        ('dungeon', '0003_dungeon_owner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dungeon',
            options={'verbose_name': '던전', 'verbose_name_plural': '던전'},
        ),
        migrations.AlterField(
            model_name='dungeon',
            name='difficulty',
            field=models.IntegerField(choices=[(1, 'Easy'), (2, 'Soso'), (3, 'Normal'), (4, 'Hard'), (5, 'Hell')], verbose_name='난이도'),
        ),
        migrations.AlterField(
            model_name='dungeon',
            name='end_date',
            field=models.DateField(verbose_name='클리어날짜'),
        ),
        migrations.AlterField(
            model_name='dungeon',
            name='impression',
            field=models.TextField(verbose_name='후기'),
        ),
        migrations.AlterField(
            model_name='dungeon',
            name='loc',
            field=models.CharField(max_length=50, verbose_name='위치'),
        ),
        migrations.AlterField(
            model_name='dungeon',
            name='name',
            field=models.CharField(default='정의되지 않은 던전', max_length=100, verbose_name='던전명'),
        ),
        migrations.AlterField(
            model_name='dungeon',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dungeons', to='me.me', verbose_name='모험가'),
        ),
        migrations.AlterField(
            model_name='dungeon',
            name='size',
            field=models.CharField(max_length=20, verbose_name='인원'),
        ),
        migrations.AlterField(
            model_name='dungeon',
            name='start_date',
            field=models.DateField(verbose_name='진입날짜'),
        ),
    ]
