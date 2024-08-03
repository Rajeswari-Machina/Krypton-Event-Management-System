# Generated by Django 5.0.7 on 2024-07-22 09:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='images')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.event')),
            ],
        ),
    ]