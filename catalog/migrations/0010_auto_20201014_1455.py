# Generated by Django 3.1 on 2020-10-14 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_auto_20201014_1441'),
    ]

    operations = [
        migrations.AddField(
            model_name='teamsroundmodel',
            name='holes3',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teamsroundmodel',
            name='holes4',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teamsroundmodel',
            name='score3',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teamsroundmodel',
            name='score4',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teamsroundmodel',
            name='team_name3',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='teamsroundmodel',
            name='team_name4',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
