# Generated by Django 3.1 on 2020-09-28 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20200928_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matchreportinput',
            name='adjective1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='matchreportinput',
            name='adjective2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='matchreportinput',
            name='animals',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
