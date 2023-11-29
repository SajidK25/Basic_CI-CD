# Generated by Django 3.1 on 2021-01-02 03:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20210102_0902'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='needhelp',
            name='time',
        ),
        migrations.AddField(
            model_name='needhelp',
            name='city',
            field=models.CharField(blank=True, help_text='city', max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='needhelp',
            name='closed',
            field=models.CharField(blank=True, help_text='time', max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='needhelp',
            name='country',
            field=models.CharField(blank=True, help_text='country', max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='needhelp',
            name='open_time',
            field=models.CharField(blank=True, help_text='time', max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='about',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 2, 3, 49, 56, 546962, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='about',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 2, 3, 49, 56, 546962, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='build',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 2, 3, 49, 56, 545967, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='build',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 2, 3, 49, 56, 545967, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='businesstonext',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 2, 3, 49, 56, 543970, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='careers',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 2, 3, 49, 56, 547971, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='careers',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 2, 3, 49, 56, 547971, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='concept',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 2, 3, 49, 56, 543970, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='concept',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 2, 3, 49, 56, 543970, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='contact',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 2, 3, 49, 56, 549954, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='contact',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 2, 3, 49, 56, 549954, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 2, 3, 49, 56, 546962, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 2, 3, 49, 56, 546962, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='design',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 2, 3, 49, 56, 544964, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='design',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 2, 3, 49, 56, 544964, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='needhelp',
            name='address',
            field=models.CharField(blank=True, help_text='address', max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='plan',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 2, 3, 49, 56, 544964, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='plan',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 2, 3, 49, 56, 544964, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='qualityassurance',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 2, 3, 49, 56, 545967, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='qualityassurance',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 2, 3, 49, 56, 545967, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='services',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 2, 3, 49, 56, 548957, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='services',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 2, 3, 49, 56, 548957, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='servicesdetail',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 2, 3, 49, 56, 548957, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='servicesdetail',
            name='publishedDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 2, 3, 49, 56, 548957, tzinfo=utc)),
        ),
    ]