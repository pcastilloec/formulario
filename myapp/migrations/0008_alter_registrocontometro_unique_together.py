# Generated by Django 5.1.4 on 2024-12-12 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_alter_registrocontometro_contometro_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='registrocontometro',
            unique_together={('FECHA', 'MAQUINA', 'HORARIO')},
        ),
    ]
