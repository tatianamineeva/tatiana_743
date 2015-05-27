# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(verbose_name=b'date_published')),
                ('time', models.TimeField(verbose_name=b'time_published')),
            ],
        ),
        migrations.CreateModel(
            name='Masters',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('middleName', models.CharField(max_length=50)),
                ('sex', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('price', models.DecimalField(max_digits=50, decimal_places=10)),
                ('description', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='ServicesOfMasters',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('master', models.ForeignKey(to='mysite.Masters')),
                ('service', models.ForeignKey(to='mysite.Services')),
            ],
        ),
        migrations.AddField(
            model_name='booking',
            name='master',
            field=models.ForeignKey(to='mysite.Masters'),
        ),
        migrations.AddField(
            model_name='booking',
            name='service',
            field=models.ForeignKey(to='mysite.Services'),
        ),
    ]
