# Generated by Django 2.1.5 on 2019-01-28 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ridesharing', '0002_ride_canbeshared'),
    ]

    operations = [
        migrations.AddField(
            model_name='ride',
            name='type',
            field=models.CharField(blank=True, choices=[('SEDAN', 'Sedan'), ('MINI', 'Minivan'), ('CROSS', 'Crossover')], default='', help_text='Vehicle type', max_length=10),
        ),
    ]
