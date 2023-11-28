# Generated by Django 4.2 on 2023-11-28 20:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bot_token',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=100, unique=True)),
                ('bot_username', models.CharField(max_length=100, unique=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'bot_token',
            },
        ),
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel_username', models.CharField(max_length=100, unique=True)),
                ('channel_name', models.CharField(max_length=100, unique=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Channel',
                'verbose_name_plural': 'Channels',
                'ordering': ['-date_created'],
            },
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=100, unique=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('username', models.CharField(blank=True, max_length=100, null=True)),
                ('language_code', models.CharField(blank=True, max_length=10, null=True)),
                ('is_bot', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('bot', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='central.bot_token')),
            ],
            options={
                'verbose_name': 'Subscriber',
                'verbose_name_plural': 'Subscribers',
                'ordering': ['-date_created'],
            },
        ),
        migrations.CreateModel(
            name='Channel_bot_settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bot', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='central.bot_token')),
                ('channel', models.ManyToManyField(blank=True, null=True, to='central.channel')),
            ],
        ),
    ]
