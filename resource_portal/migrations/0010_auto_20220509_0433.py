# Generated by Django 3.0.8 on 2022-05-09 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resource_portal', '0009_auto_20220509_0424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='department',
            field=models.CharField(choices=[('None', 'None'), ('Computer Science and Engineering', 'Computer Science and Engineering'), ('Information Technology', 'Information Technology'), ('Electronics and Communication Engineering', 'Electronics and Communication Engineering'), ('Mechanical Engineering', 'Mechanical Engineering'), ('Electrical & Electronics Engineering', 'Electrical & Electronics Engineering'), ('Electrical Engineering', 'Electrical Engineering'), ('Civil Engineering', 'Civil Engineering')], default='None', max_length=100),
        ),
    ]