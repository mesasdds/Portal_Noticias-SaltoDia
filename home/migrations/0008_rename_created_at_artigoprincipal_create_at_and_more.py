# Generated by Django 4.2 on 2023-05-04 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_artigoprincipal_created_at_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artigoprincipal',
            old_name='created_at',
            new_name='create_at',
        ),
        migrations.RenameField(
            model_name='artigoprincipal',
            old_name='updated_at',
            new_name='update_at',
        ),
        migrations.RenameField(
            model_name='artigosecundario',
            old_name='created_at',
            new_name='create_at',
        ),
        migrations.RenameField(
            model_name='artigosecundario',
            old_name='updated_at',
            new_name='update_at',
        ),
        migrations.RenameField(
            model_name='artigoterceiro',
            old_name='created_at',
            new_name='create_at',
        ),
        migrations.RenameField(
            model_name='artigoterceiro',
            old_name='updated_at',
            new_name='update_at',
        ),
    ]
