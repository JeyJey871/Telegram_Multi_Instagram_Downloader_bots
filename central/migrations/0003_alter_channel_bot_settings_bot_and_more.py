# Generated by Django 4.2 on 2023-11-30 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('central', '0002_bot_token_start_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel_bot_settings',
            name='bot',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='central.bot_token'),
        ),
        migrations.CreateModel(
            name='User_subscribe_channel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscribe', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('channel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='central.channel')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='central.subscriber')),
            ],
            options={
                'db_table': 'user_subscribe_channel',
                'unique_together': {('user', 'channel')},
            },
        ),
    ]
