# Generated by Django 4.2.2 on 2023-06-21 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('qna', '0003_rename_created_at_answer_created_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={'verbose_name': '답변', 'verbose_name_plural': '답변'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': '질문', 'verbose_name_plural': '질문'},
        ),
        migrations.RemoveField(
            model_name='question',
            name='is_completed',
        ),
        migrations.AlterField(
            model_name='answer',
            name='content',
            field=models.TextField(verbose_name='내용'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='qna.question', verbose_name='질문'),
        ),
        migrations.AlterField(
            model_name='question',
            name='content',
            field=models.TextField(verbose_name='내용'),
        ),
        migrations.AlterField(
            model_name='question',
            name='ip',
            field=models.CharField(max_length=50, null=True, verbose_name='세계'),
        ),
    ]
