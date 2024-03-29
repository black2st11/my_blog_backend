# Generated by Django 4.2.2 on 2023-06-22 04:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hunter', '0001_initial'),
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dungeon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('deleted', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(default='정의되지 않은 던전', max_length=100, verbose_name='던전명')),
                ('start_date', models.DateField(verbose_name='진입날짜')),
                ('end_date', models.DateField(verbose_name='클리어날짜')),
                ('difficulty', models.IntegerField(choices=[(1, 'Easy'), (2, 'Soso'), (3, 'Normal'), (4, 'Hard'), (5, 'Hell')], verbose_name='난이도')),
                ('size', models.CharField(max_length=20, verbose_name='인원')),
                ('address', models.CharField(max_length=50, verbose_name='위치')),
                ('impression', models.TextField(verbose_name='후기')),
            ],
            options={
                'verbose_name': '던전',
                'verbose_name_plural': '던전',
                'db_table': 'dungeon',
            },
        ),
        migrations.CreateModel(
            name='DungeonSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('deleted', models.DateTimeField(blank=True, null=True)),
                ('dungeon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dungeon.dungeon')),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.skill')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DungeonDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('deleted', models.DateTimeField(blank=True, null=True)),
                ('description', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.description')),
                ('dungeon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dungeon.dungeon')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DungeonAttach',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('deleted', models.DateTimeField(blank=True, null=True)),
                ('attach', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.attach')),
                ('dungeon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dungeon.dungeon')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='dungeon',
            name='attachs',
            field=models.ManyToManyField(related_name='dungeons', through='dungeon.DungeonAttach', to='info.attach'),
        ),
        migrations.AddField(
            model_name='dungeon',
            name='descriptions',
            field=models.ManyToManyField(related_name='dungeons', through='dungeon.DungeonDescription', to='info.description'),
        ),
        migrations.AddField(
            model_name='dungeon',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dungeons', to='hunter.hunter', verbose_name='모험가'),
        ),
        migrations.AddField(
            model_name='dungeon',
            name='skills',
            field=models.ManyToManyField(related_name='dungeons', through='dungeon.DungeonSkill', to='info.skill'),
        ),
    ]
