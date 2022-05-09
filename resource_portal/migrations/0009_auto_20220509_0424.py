# Generated by Django 3.0.8 on 2022-05-09 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resource_portal', '0008_resource_favourite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='year',
            field=models.CharField(choices=[('None', 'None'), ('1st Year', '1st Year'), ('2nd Year', '2nd Year'), ('3rd Year', '3rd Year'), ('4th Year', '4th Year')], default='None', max_length=10),
        ),
    ]