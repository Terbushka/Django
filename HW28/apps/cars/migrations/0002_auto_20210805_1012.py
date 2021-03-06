# Generated by Django 3.2.5 on 2021-08-05 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='car_segments',
            field=models.CharField(choices=[('segment A', 'segment A'), ('segment B', 'segment B'), ('segment C', 'segment C'), ('segment D', 'segment D'), ('segment E', 'segment E'), ('segment F', 'segment F')], default='segment B', max_length=50),
        ),
        migrations.AddField(
            model_name='car',
            name='pollutant_class',
            field=models.CharField(choices=[('class A', 'class A'), ('class B', 'class B'), ('class C', 'class C'), ('class D', 'class D'), ('class E', 'class E'), ('class F', 'class F'), ('class G', 'class G')], default='class B', max_length=50),
        ),
    ]