# Generated by Django 3.2.6 on 2021-09-12 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0026_sold_shipping_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='sold',
            name='shipping_country',
            field=models.CharField(choices=[('Malaysia1', 'Malaysia1'), ('Malaysia2', 'Malaysia2'), ('Singapore', 'Singapore'), ('Brunel', 'Brunel')], default='Malaysia1', max_length=9),
        ),
        migrations.AddField(
            model_name='sold',
            name='shipping_rate',
            field=models.CharField(choices=[('Normal', 'Normal'), ('Sensitive', 'Sensitive')], default='Normal', max_length=9),
        ),
    ]
