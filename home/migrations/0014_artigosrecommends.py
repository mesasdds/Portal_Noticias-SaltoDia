# Generated by Django 4.2 on 2023-05-04 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_alter_artigoprincipal_imagem_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArtigosRecommends',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('texto', models.TextField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='media/')),
            ],
        ),
    ]
