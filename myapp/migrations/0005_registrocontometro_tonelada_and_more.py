# Generated by Django 5.1.4 on 2024-12-11 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_registrocontometro'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrocontometro',
            name='TONELADA',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registrocontometro',
            name='TONELADA2',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
