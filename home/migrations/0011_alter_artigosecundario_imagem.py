# Generated by Django 4.2 on 2023-05-04 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_artigosecundario_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artigosecundario',
            name='imagem',
            field=models.ImageField(blank=True, upload_to='media/'),
        ),
    ]
