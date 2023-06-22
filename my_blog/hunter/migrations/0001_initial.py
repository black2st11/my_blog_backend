# Generated by Django 4.2.2 on 2023-06-22 04:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArchDesc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('deleted', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Archiving',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('deleted', models.DateTimeField(blank=True, null=True)),
                ('category', models.CharField(max_length=20, verbose_name='주제명')),
                ('descriptions', models.ManyToManyField(related_name='archivings', through='hunter.ArchDesc', to='info.description')),
            ],
            options={
                'verbose_name': '주제',
                'verbose_name_plural': '주제',
                'db_table': 'archiving',
            },
        ),
        migrations.CreateModel(
            name='Hunter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('deleted', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(default='', max_length=30, verbose_name='이름')),
                ('phone', models.CharField(default='00000000000', max_length=12, verbose_name='연락처')),
                ('birth', models.DateField(verbose_name='생년월일')),
                ('email', models.EmailField(max_length=254, verbose_name='이메일')),
                ('edu', models.CharField(default='', max_length=100, verbose_name='학력')),
                ('address', models.CharField(default='', max_length=100, verbose_name='주소')),
                ('archiving', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hunter', to='hunter.archiving')),
            ],
            options={
                'verbose_name': '모험가',
                'verbose_name_plural': '모험가',
            },
        ),
        migrations.CreateModel(
            name='MySkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('deleted', models.DateTimeField(blank=True, null=True)),
                ('hunter', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hunter.hunter')),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='info.skill')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='hunter',
            name='skills',
            field=models.ManyToManyField(related_name='hunter', through='hunter.MySkill', to='info.skill'),
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('deleted', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(max_length=50, verbose_name='훈련장명')),
                ('major', models.CharField(max_length=50, verbose_name='전공')),
                ('point', models.DecimalField(decimal_places=2, max_digits=3, verbose_name='학점')),
                ('full_point', models.DecimalField(decimal_places=2, max_digits=3, verbose_name='전체학점')),
                ('started', models.DateField(verbose_name='시작날짜')),
                ('ended', models.DateField(blank=True, null=True, verbose_name='종료날짜')),
                ('hunter', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='educations', to='hunter.hunter', verbose_name='모험가')),
            ],
            options={
                'verbose_name': '훈련장',
                'verbose_name_plural': '훈련장',
            },
        ),
        migrations.AddField(
            model_name='archiving',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='archivings', to='hunter.hunter', verbose_name='모험가'),
        ),
        migrations.AddField(
            model_name='archdesc',
            name='archiving',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hunter.archiving'),
        ),
        migrations.AddField(
            model_name='archdesc',
            name='description',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='info.description'),
        ),
    ]
