# Generated by Django 4.2.2 on 2023-06-21 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('me', '0003_rename_loc_me_address_archdesc_created_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='archiving',
            options={'verbose_name': '주제', 'verbose_name_plural': '주제'},
        ),
        migrations.AlterModelOptions(
            name='education',
            options={'verbose_name': '훈련장', 'verbose_name_plural': '훈련장'},
        ),
        migrations.AlterModelOptions(
            name='me',
            options={'verbose_name': '유저', 'verbose_name_plural': '유저'},
        ),
        migrations.AddField(
            model_name='archiving',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='archivings', to='me.me'),
            preserve_default=False,
        ),
    ]
