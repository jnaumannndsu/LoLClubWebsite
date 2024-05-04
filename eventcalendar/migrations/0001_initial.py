# Generated by Django 5.0.3 on 2024-05-04 18:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('eventID', models.BigAutoField(primary_key=True, serialize=False)),
                ('startTime', models.DateTimeField()),
                ('endTime', models.DateTimeField()),
                ('eventName', models.CharField(default='New Event', max_length=160)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('event', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='eventcalendar.event')),
                ('team', models.CharField(blank=True, choices=[('v', 'Varsity'), ('j', 'Junior Varsity'), ('c', 'C Team'), ('d', 'D Team'), ('o', 'Other')], help_text='Team playing', max_length=1)),
                ('league', models.CharField(blank=True, choices=[('c', 'CCL'), ('n', 'NECC'), ('e', 'NACE'), ('o', 'Other')], help_text='What League are they competing in', max_length=1)),
                ('status', models.CharField(blank=True, choices=[('m', 'Main'), ('a', 'Alt'), ('n', 'None')], default='n', help_text='Where streamed', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Lan',
            fields=[
                ('event', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='eventcalendar.event')),
                ('location', models.CharField(max_length=320)),
            ],
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('event', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='eventcalendar.event')),
                ('status', models.CharField(blank=True, choices=[('m', 'Main'), ('a', 'Alt'), ('n', 'None')], default='n', help_text='Where streamed', max_length=1)),
                ('signup', models.URLField()),
            ],
        ),
    ]
