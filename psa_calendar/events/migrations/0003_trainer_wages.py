# Generated by Django 3.1.1 on 2020-11-02 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20201102_1637'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainer',
            name='wages',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
