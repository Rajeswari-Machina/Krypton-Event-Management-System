# Generated by Django 5.0.7 on 2024-07-30 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_alter_photos_event_alter_profile_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
