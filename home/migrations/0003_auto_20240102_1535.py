# Generated by Django 3.1 on 2024-01-02 15:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20240102_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 2, 15, 35, 36, 945569, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='about',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 2, 15, 35, 36, 945629, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 2, 15, 35, 36, 952520, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 2, 15, 35, 36, 952564, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='blogsdetail',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 2, 15, 35, 36, 953598, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='blogsdetail',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 2, 15, 35, 36, 953642, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='build',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 2, 15, 35, 36, 942207, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='build',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 2, 15, 35, 36, 942270, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='businesstonext',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 2, 15, 35, 36, 937828, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='careers',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 2, 15, 35, 36, 946646, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='careers',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 2, 15, 35, 36, 946691, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='concept',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 2, 15, 35, 36, 939072, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='concept',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 2, 15, 35, 36, 939117, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='contact',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 2, 15, 35, 36, 950268, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='contact',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 2, 15, 35, 36, 950312, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 2, 15, 35, 36, 944342, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 2, 15, 35, 36, 944386, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='design',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 2, 15, 35, 36, 941212, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='design',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 2, 15, 35, 36, 941256, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='plan',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 2, 15, 35, 36, 940149, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='plan',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 2, 15, 35, 36, 940195, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='qualityassurance',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 2, 15, 35, 36, 943283, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='qualityassurance',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 2, 15, 35, 36, 943327, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='services',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 2, 15, 35, 36, 948054, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='services',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 2, 15, 35, 36, 948097, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='servicesdetail',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 2, 15, 35, 36, 949183, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='servicesdetail',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 2, 15, 35, 36, 949248, tzinfo=utc)),
        ),
    ]
