# Generated by Django 3.2.6 on 2021-09-02 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0016_alter_sold_shipped_to_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sold',
            name='shipped_to_client',
            field=models.CharField(choices=[('NOT SHIPPED', 'Order is on the warehouse'), ('SHIPPED', 'Order has been shipped out')], default='NOT SHIPPED', max_length=11),
        ),
    ]
