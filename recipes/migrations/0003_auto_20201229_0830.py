# Generated by Django 3.1.4 on 2020-12-29 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_auto_20201229_0655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='cook_time',
            field=models.DurationField(),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='prep_time',
            field=models.DurationField(),
        ),
    ]
