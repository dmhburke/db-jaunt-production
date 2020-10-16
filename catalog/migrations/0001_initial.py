# Generated by Django 3.1 on 2020-08-26 22:30

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminHoleDetails',
            fields=[
                ('roundNum', models.IntegerField(primary_key=True, serialize=False)),
                ('courseName', models.CharField(blank=True, max_length=100, null=True)),
                ('tussleName', models.CharField(blank=True, max_length=100, null=True)),
                ('scorecardLink', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Input_TourDetailsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tour_name', models.CharField(blank=True, max_length=200, null=True)),
                ('points_link', models.CharField(blank=True, max_length=200, null=True)),
                ('map_link', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LeaderBoardModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player', models.CharField(blank=True, max_length=30, null=True)),
                ('rd1_golf', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('rd1_ctpld', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('rd1_bonus', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('rd1_total', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('rd2_golf', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('rd2_ctpld', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('rd2_bonus', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('rd2_total', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('rd3_golf', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('rd3_ctpld', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('rd3_bonus', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('rd3_total', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('social', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('best_dressed', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('tipping', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('other_total', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('overall_total', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PlayerModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(max_length=30)),
                ('HC', models.IntegerField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='playerimages')),
                ('jacket', models.CharField(blank=True, choices=[('YES', 'Yes'), ('NO', 'No')], max_length=10, null=True)),
                ('highfinish', models.IntegerField(blank=True, null=True)),
                ('tournum', models.IntegerField(blank=True, null=True)),
                ('nickname', models.CharField(blank=True, max_length=30, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('total', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=6, null=True)),
            ],
            options={
                'ordering': ['-total'],
            },
        ),
        migrations.CreateModel(
            name='Rd1EnduranceModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slot', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(blank=True, choices=[('YES', 'Yes'), ('NO', 'No')], max_length=30, null=True)),
                ('firstnine_stbl', models.IntegerField(blank=True, null=True)),
                ('secondnine_stbl', models.IntegerField(blank=True, null=True)),
                ('endurance_score', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rd1HoleModel',
            fields=[
                ('number', models.IntegerField(primary_key=True, serialize=False)),
                ('par', models.IntegerField(blank=True, null=True)),
                ('index', models.IntegerField(blank=True, null=True)),
                ('meters', models.IntegerField(blank=True, null=True)),
                ('CTP', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(4)])),
                ('LD', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(2)])),
                ('tussle', models.CharField(blank=True, choices=[('YES', 'Yes'), ('NO', 'No')], max_length=10, null=True)),
            ],
            options={
                'ordering': ['number'],
            },
        ),
        migrations.CreateModel(
            name='Rd2HoleModel',
            fields=[
                ('number', models.IntegerField(primary_key=True, serialize=False)),
                ('par', models.IntegerField(blank=True, null=True)),
                ('index', models.IntegerField(blank=True, null=True)),
                ('meters', models.IntegerField(blank=True, null=True)),
                ('CTP', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(4)])),
                ('LD', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(2)])),
                ('tussle', models.CharField(blank=True, choices=[('YES', 'Yes'), ('NO', 'No')], max_length=10, null=True)),
            ],
            options={
                'ordering': ['number'],
            },
        ),
        migrations.CreateModel(
            name='Rd3HoleModel',
            fields=[
                ('number', models.IntegerField(primary_key=True, serialize=False)),
                ('par', models.IntegerField(blank=True, null=True)),
                ('index', models.IntegerField(blank=True, null=True)),
                ('meters', models.IntegerField(blank=True, null=True)),
                ('CTP', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(4)])),
                ('LD', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(2)])),
                ('tussle', models.CharField(blank=True, choices=[('YES', 'Yes'), ('NO', 'No')], max_length=10, null=True)),
            ],
            options={
                'ordering': ['number'],
            },
        ),
        migrations.CreateModel(
            name='Rd4HoleModel',
            fields=[
                ('number', models.IntegerField(primary_key=True, serialize=False)),
                ('par', models.IntegerField(blank=True, null=True)),
                ('index', models.IntegerField(blank=True, null=True)),
                ('meters', models.IntegerField(blank=True, null=True)),
                ('CTP', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(4)])),
                ('LD', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(2)])),
                ('tussle', models.CharField(blank=True, choices=[('YES', 'Yes'), ('NO', 'No')], max_length=10, null=True)),
            ],
            options={
                'ordering': ['number'],
            },
        ),
        migrations.CreateModel(
            name='SportsTippingResultsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='result', max_length=20, null=True)),
                ('result1', models.CharField(blank=True, choices=[('NOT_COMPLETE', 'No result'), ('NETS', 'Nets'), ('ROCKETS', 'Rockets')], max_length=20, null=True)),
                ('result2', models.CharField(blank=True, choices=[('NOT_COMPLETE', 'No result'), ('LIGHTNING', 'Lightning'), ('ISLANDERS', 'Islanders')], max_length=20, null=True)),
                ('result3', models.CharField(blank=True, choices=[('NOT_COMPLETE', 'No result'), ('OILERS', 'Oilers'), ('PENGUINS', 'Penguins')], max_length=20, null=True)),
                ('result4', models.CharField(blank=True, choices=[('NOT_COMPLETE', 'No result'), ('RAPTORS', 'Raptors'), ('BUCKS', 'Bucks')], max_length=20, null=True)),
                ('result5', models.CharField(blank=True, choices=[('NOT_COMPLETE', 'No result'), ('CRYSTAL_PALACE', 'Crystal Palace'), ('LEICESTER_CITY', 'Leicester City'), ('DRAW', 'Draw')], max_length=20, null=True)),
                ('result6', models.CharField(blank=True, choices=[('NOT_COMPLETE', 'No result'), ('ARSENAL', 'Arsenal'), ('WOLVERHAMPTON', 'Wolverhampton'), ('DRAW', 'Draw')], max_length=20, null=True)),
                ('result7', models.CharField(blank=True, choices=[('NOT_COMPLETE', 'No result'), ('ENGLAND', 'England'), ('SOUTH_AFRICA', 'South Africa')], max_length=20, null=True)),
                ('result8', models.CharField(blank=True, choices=[('NOT_COMPLETE', 'No result'), ('OLE_MISS', 'Ole Miss'), ('AUBURN', 'Auburn')], max_length=20, null=True)),
                ('result9', models.CharField(blank=True, choices=[('NOT_COMPLETE', 'No result'), ('OREGON', 'Oregon'), ('USC', 'USC')], max_length=20, null=True)),
                ('result10', models.CharField(blank=True, choices=[('NOT_COMPLETE', 'No result'), ('MIAMI', 'Miami'), ('FLORIDA_STATE', 'Florida State')], max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SportsTippingScoreModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(blank=True, null=True)),
                ('total', models.IntegerField(blank=True, null=True)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.playermodel')),
            ],
            options={
                'ordering': ['-total', 'time'],
            },
        ),
        migrations.CreateModel(
            name='SportsTippingModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(blank=True, max_length=30, null=True)),
                ('game1', models.CharField(blank=True, choices=[('', 'Select result'), ('NETS', 'Nets'), ('ROCKETS', 'Rockets')], max_length=20, null=True)),
                ('game2', models.CharField(blank=True, choices=[('', 'Select result'), ('LIGHTNING', 'Lightning'), ('ISLANDERS', 'Islanders')], max_length=20, null=True)),
                ('game3', models.CharField(blank=True, choices=[('', 'Select result'), ('OILERS', 'Oilers'), ('PENGUINS', 'Penguins')], max_length=20, null=True)),
                ('game4', models.CharField(blank=True, choices=[('', 'Select result'), ('RAPTORS', 'Raptors'), ('BUCKS', 'Bucks')], max_length=20, null=True)),
                ('game5', models.CharField(blank=True, choices=[('', 'Select result'), ('CRYSTAL_PALACE', 'Crystal Palace'), ('LEICESTER_CITY', 'Leicester City'), ('DRAW', 'Draw')], max_length=20, null=True)),
                ('game6', models.CharField(blank=True, choices=[('', 'Select result'), ('ARSENAL', 'Arsenal'), ('WOLVERHAMPTON', 'Wolverhampton'), ('DRAW', 'Draw')], max_length=20, null=True)),
                ('game7', models.CharField(blank=True, choices=[('', 'Select result'), ('ENGLAND', 'England'), ('SOUTH_AFRICA', 'South Africa')], max_length=20, null=True)),
                ('game8', models.CharField(blank=True, choices=[('', 'Select result'), ('OLE_MISS', 'Ole Miss'), ('AUBURN', 'Auburn')], max_length=20, null=True)),
                ('game9', models.CharField(blank=True, choices=[('', 'Select result'), ('OREGON', 'Oregon'), ('USC', 'USC')], max_length=20, null=True)),
                ('game10', models.CharField(blank=True, choices=[('', 'Select result'), ('MIAMI', 'Miami'), ('FLORIDA_STATE', 'Florida State')], max_length=20, null=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.playermodel')),
            ],
        ),
        migrations.CreateModel(
            name='Rd4StablefordModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slot1_stbl', models.IntegerField(blank=True, null=True)),
                ('slot2_stbl', models.IntegerField(blank=True, null=True)),
                ('slot3_stbl', models.IntegerField(blank=True, null=True)),
                ('slot4_stbl', models.IntegerField(blank=True, null=True)),
                ('slot5_stbl', models.IntegerField(blank=True, null=True)),
                ('slot6_stbl', models.IntegerField(blank=True, null=True)),
                ('slot7_stbl', models.IntegerField(blank=True, null=True)),
                ('slot8_stbl', models.IntegerField(blank=True, null=True)),
                ('slot9_stbl', models.IntegerField(blank=True, null=True)),
                ('slot10_stbl', models.IntegerField(blank=True, null=True)),
                ('slot11_stbl', models.IntegerField(blank=True, null=True)),
                ('slot12_stbl', models.IntegerField(blank=True, null=True)),
                ('hole', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.rd4holemodel')),
            ],
        ),
        migrations.CreateModel(
            name='Rd4SlotModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_slot', models.IntegerField(unique=True, validators=[django.core.validators.MaxValueValidator(12), django.core.validators.MinValueValidator(1)])),
                ('player_holesplayed', models.IntegerField(blank=True, null=True)),
                ('player_score', models.IntegerField(blank=True, null=True)),
                ('player_stbl', models.IntegerField(blank=True, null=True)),
                ('player_rankscore', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('tussle_score', models.IntegerField(blank=True, null=True)),
                ('player_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.playermodel')),
            ],
            options={
                'ordering': ['-player_rankscore', '-tussle_score', 'player_name__HC'],
            },
        ),
        migrations.CreateModel(
            name='Rd4ScoreModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slot1_score', models.IntegerField(blank=True, null=True)),
                ('slot2_score', models.IntegerField(blank=True, null=True)),
                ('slot3_score', models.IntegerField(blank=True, null=True)),
                ('slot4_score', models.IntegerField(blank=True, null=True)),
                ('slot5_score', models.IntegerField(blank=True, null=True)),
                ('slot6_score', models.IntegerField(blank=True, null=True)),
                ('slot7_score', models.IntegerField(blank=True, null=True)),
                ('slot8_score', models.IntegerField(blank=True, null=True)),
                ('slot9_score', models.IntegerField(blank=True, null=True)),
                ('slot10_score', models.IntegerField(blank=True, null=True)),
                ('slot11_score', models.IntegerField(blank=True, null=True)),
                ('slot12_score', models.IntegerField(blank=True, null=True)),
                ('ctp', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Rd4ctp', to='catalog.playermodel')),
                ('hole', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.rd4holemodel')),
                ('ld', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Rd4ld', to='catalog.playermodel')),
            ],
        ),
        migrations.CreateModel(
            name='Rd3StablefordModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slot1_stbl', models.IntegerField(blank=True, null=True)),
                ('slot2_stbl', models.IntegerField(blank=True, null=True)),
                ('slot3_stbl', models.IntegerField(blank=True, null=True)),
                ('slot4_stbl', models.IntegerField(blank=True, null=True)),
                ('slot5_stbl', models.IntegerField(blank=True, null=True)),
                ('slot6_stbl', models.IntegerField(blank=True, null=True)),
                ('slot7_stbl', models.IntegerField(blank=True, null=True)),
                ('slot8_stbl', models.IntegerField(blank=True, null=True)),
                ('slot9_stbl', models.IntegerField(blank=True, null=True)),
                ('slot10_stbl', models.IntegerField(blank=True, null=True)),
                ('slot11_stbl', models.IntegerField(blank=True, null=True)),
                ('slot12_stbl', models.IntegerField(blank=True, null=True)),
                ('hole', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.rd3holemodel')),
            ],
        ),
        migrations.CreateModel(
            name='Rd3SlotModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_slot', models.IntegerField(unique=True, validators=[django.core.validators.MaxValueValidator(12), django.core.validators.MinValueValidator(1)])),
                ('player_holesplayed', models.IntegerField(blank=True, null=True)),
                ('player_score', models.IntegerField(blank=True, null=True)),
                ('player_stbl', models.IntegerField(blank=True, null=True)),
                ('player_rankscore', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('tussle_score', models.IntegerField(blank=True, null=True)),
                ('player_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.playermodel')),
            ],
            options={
                'ordering': ['-player_rankscore', '-tussle_score', 'player_name__HC'],
            },
        ),
        migrations.CreateModel(
            name='Rd3ScoreModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slot1_score', models.IntegerField(blank=True, null=True)),
                ('slot2_score', models.IntegerField(blank=True, null=True)),
                ('slot3_score', models.IntegerField(blank=True, null=True)),
                ('slot4_score', models.IntegerField(blank=True, null=True)),
                ('slot5_score', models.IntegerField(blank=True, null=True)),
                ('slot6_score', models.IntegerField(blank=True, null=True)),
                ('slot7_score', models.IntegerField(blank=True, null=True)),
                ('slot8_score', models.IntegerField(blank=True, null=True)),
                ('slot9_score', models.IntegerField(blank=True, null=True)),
                ('slot10_score', models.IntegerField(blank=True, null=True)),
                ('slot11_score', models.IntegerField(blank=True, null=True)),
                ('slot12_score', models.IntegerField(blank=True, null=True)),
                ('ctp', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='RD3ctp', to='catalog.playermodel')),
                ('hole', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.rd3holemodel')),
                ('ld', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='RD3ld', to='catalog.playermodel')),
            ],
        ),
        migrations.CreateModel(
            name='Rd2StablefordModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slot1_stbl', models.IntegerField(blank=True, null=True)),
                ('slot2_stbl', models.IntegerField(blank=True, null=True)),
                ('slot3_stbl', models.IntegerField(blank=True, null=True)),
                ('slot4_stbl', models.IntegerField(blank=True, null=True)),
                ('slot5_stbl', models.IntegerField(blank=True, null=True)),
                ('slot6_stbl', models.IntegerField(blank=True, null=True)),
                ('slot7_stbl', models.IntegerField(blank=True, null=True)),
                ('slot8_stbl', models.IntegerField(blank=True, null=True)),
                ('slot9_stbl', models.IntegerField(blank=True, null=True)),
                ('slot10_stbl', models.IntegerField(blank=True, null=True)),
                ('slot11_stbl', models.IntegerField(blank=True, null=True)),
                ('slot12_stbl', models.IntegerField(blank=True, null=True)),
                ('hole', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.rd2holemodel')),
            ],
        ),
        migrations.CreateModel(
            name='Rd2SlotModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_slot', models.IntegerField(unique=True, validators=[django.core.validators.MaxValueValidator(12), django.core.validators.MinValueValidator(1)])),
                ('player_holesplayed', models.IntegerField(blank=True, null=True)),
                ('player_score', models.IntegerField(blank=True, null=True)),
                ('player_stbl', models.IntegerField(blank=True, null=True)),
                ('player_rankscore', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('tussle_score', models.IntegerField(blank=True, null=True)),
                ('player_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.playermodel')),
            ],
            options={
                'ordering': ['-player_rankscore', '-tussle_score', 'player_name__HC'],
            },
        ),
        migrations.CreateModel(
            name='Rd2ScoreModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slot1_score', models.IntegerField(blank=True, null=True)),
                ('slot2_score', models.IntegerField(blank=True, null=True)),
                ('slot3_score', models.IntegerField(blank=True, null=True)),
                ('slot4_score', models.IntegerField(blank=True, null=True)),
                ('slot5_score', models.IntegerField(blank=True, null=True)),
                ('slot6_score', models.IntegerField(blank=True, null=True)),
                ('slot7_score', models.IntegerField(blank=True, null=True)),
                ('slot8_score', models.IntegerField(blank=True, null=True)),
                ('slot9_score', models.IntegerField(blank=True, null=True)),
                ('slot10_score', models.IntegerField(blank=True, null=True)),
                ('slot11_score', models.IntegerField(blank=True, null=True)),
                ('slot12_score', models.IntegerField(blank=True, null=True)),
                ('ctp', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='RD2ctp', to='catalog.playermodel')),
                ('hole', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.rd2holemodel')),
                ('ld', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='RD2ld', to='catalog.playermodel')),
            ],
        ),
        migrations.CreateModel(
            name='Rd1StablefordModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slot1_stbl', models.IntegerField(blank=True, null=True)),
                ('slot2_stbl', models.IntegerField(blank=True, null=True)),
                ('slot3_stbl', models.IntegerField(blank=True, null=True)),
                ('slot4_stbl', models.IntegerField(blank=True, null=True)),
                ('slot5_stbl', models.IntegerField(blank=True, null=True)),
                ('slot6_stbl', models.IntegerField(blank=True, null=True)),
                ('slot7_stbl', models.IntegerField(blank=True, null=True)),
                ('slot8_stbl', models.IntegerField(blank=True, null=True)),
                ('slot9_stbl', models.IntegerField(blank=True, null=True)),
                ('slot10_stbl', models.IntegerField(blank=True, null=True)),
                ('slot11_stbl', models.IntegerField(blank=True, null=True)),
                ('slot12_stbl', models.IntegerField(blank=True, null=True)),
                ('hole', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.rd1holemodel')),
            ],
        ),
        migrations.CreateModel(
            name='Rd1SlotModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_slot', models.IntegerField(unique=True, validators=[django.core.validators.MaxValueValidator(12), django.core.validators.MinValueValidator(1)])),
                ('player_holesplayed', models.IntegerField(blank=True, null=True)),
                ('player_score', models.IntegerField(blank=True, null=True)),
                ('player_stbl', models.IntegerField(blank=True, null=True)),
                ('player_rankscore', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('tussle_score', models.IntegerField(blank=True, null=True)),
                ('endurance_score', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('player_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.playermodel')),
            ],
            options={
                'ordering': ['-player_rankscore', '-tussle_score', 'player_name__HC'],
            },
        ),
        migrations.CreateModel(
            name='Rd1ScoreModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slot1_score', models.IntegerField(blank=True, null=True)),
                ('slot2_score', models.IntegerField(blank=True, null=True)),
                ('slot3_score', models.IntegerField(blank=True, null=True)),
                ('slot4_score', models.IntegerField(blank=True, null=True)),
                ('slot5_score', models.IntegerField(blank=True, null=True)),
                ('slot6_score', models.IntegerField(blank=True, null=True)),
                ('slot7_score', models.IntegerField(blank=True, null=True)),
                ('slot8_score', models.IntegerField(blank=True, null=True)),
                ('slot9_score', models.IntegerField(blank=True, null=True)),
                ('slot10_score', models.IntegerField(blank=True, null=True)),
                ('slot11_score', models.IntegerField(blank=True, null=True)),
                ('slot12_score', models.IntegerField(blank=True, null=True)),
                ('ctp', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='RD1ctp', to='catalog.playermodel')),
                ('hole', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.rd1holemodel')),
                ('ld', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='RD1ld', to='catalog.playermodel')),
            ],
        ),
        migrations.CreateModel(
            name='EventEntryModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(blank=True, null=True)),
                ('event', models.CharField(max_length=30)),
                ('category', models.CharField(blank=True, choices=[('Round1Golf', 'Round1Golf'), ('Round1CTPLD', 'Round1CTPLD'), ('Round1_Bonus', 'Round1_Bonus'), ('Round2Golf', 'Round2Golf'), ('Round2CTPLD', 'Round2CTPLD'), ('Round2_Bonus', 'Round2_Bonus'), ('Round3Golf', 'Round3Golf'), ('Round3CTPLD', 'Round3CTPLD'), ('Round3_Bonus', 'Round3_Bonus'), ('Social', 'Social'), ('Best_dressed', 'Best_dressed'), ('Tipping', 'Tipping')], max_length=30, null=True)),
                ('points', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('winner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.playermodel')),
            ],
        ),
    ]
