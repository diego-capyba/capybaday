# Generated by Django 4.1.2 on 2022-10-20 23:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='nome')),
            ],
            options={
                'verbose_name': 'local',
                'verbose_name_plural': 'locais',
            },
        ),
        migrations.CreateModel(
            name='Rider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='nome')),
            ],
            options={
                'verbose_name': 'montador',
                'verbose_name_plural': 'montadores',
            },
        ),
        migrations.CreateModel(
            name='Dragon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='nome')),
                ('color', models.CharField(choices=[('red', 'Red'), ('green', 'Green'), ('blue', 'Blue')], max_length=10, verbose_name='cor')),
                ('weight', models.DecimalField(decimal_places=3, help_text='tons', max_digits=5, verbose_name='peso')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dragon.location', verbose_name='local')),
                ('riders', models.ManyToManyField(to='dragon.rider', verbose_name='montadores')),
            ],
            options={
                'verbose_name': 'dragão',
                'verbose_name_plural': 'dragões',
            },
        ),
    ]
