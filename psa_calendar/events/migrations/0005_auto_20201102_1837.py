# Generated by Django 3.1.1 on 2020-11-02 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20201102_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainer',
            name='wages',
            field=models.FloatField(blank=True, null=True),
        ),
    ]