# Generated by Django 5.1.4 on 2024-12-11 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_registrocontometro_tonelada_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrocontometro',
            name='CONTOMETRO2',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]