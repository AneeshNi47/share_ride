# Generated by Django 4.1.3 on 2022-11-30 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ride_request', '0002_alter_riderequest_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='riderequest',
            unique_together=set(),
        ),
    ]
