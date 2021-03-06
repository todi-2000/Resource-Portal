# Generated by Django 3.0.8 on 2020-07-28 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20200728_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='department',
            field=models.CharField(choices=[('None', 'None'), ('CS', 'Computer Science and Engineering'), ('IT', 'Information Technology'), ('EC', 'Electronics and Communication Engineering'), ('ME', 'Mechanical Engineering'), ('EEE', 'Electrical & Electronics Engineering'), ('EE', 'Electrical Engineering'), ('CE', 'Civil Engineering')], default='None', max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='year',
            field=models.CharField(choices=[('None', 'None'), ('1st', '1st Year'), ('2nd', '2nd Year'), ('3rd', '3rd Year'), ('4th', '4th Year')], default='None', max_length=15),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='department',
            field=models.CharField(choices=[('None', 'None'), ('CS', 'Computer Science and Engineering'), ('IT', 'Information Technology'), ('EC', 'Electronics and Communication Engineering'), ('ME', 'Mechanical Engineering'), ('EEE', 'Electrical & Electronics Engineering'), ('EE', 'Electrical Engineering'), ('CE', 'Civil Engineering')], default='None', max_length=500),
        ),
    ]
