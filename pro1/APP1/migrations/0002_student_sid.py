# Generated by Django 4.1.5 on 2023-01-10 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='sid',
            field=models.IntegerField(default=1, unique=True),
            preserve_default=False,
        ),
    ]
