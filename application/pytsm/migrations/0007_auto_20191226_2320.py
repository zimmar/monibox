# Generated by Django 3.0.1 on 2019-12-26 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pytsm', '0006_auto_20191226_2304'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cfgoverview',
            name='active',
        ),
        migrations.AlterField(
            model_name='joblist',
            name='lastrun',
            field=models.DateTimeField(help_text='', verbose_name='Lastrun'),
        ),
        migrations.AlterField(
            model_name='joblist',
            name='nextrun',
            field=models.DateTimeField(help_text='', verbose_name='Nextrun'),
        ),
        migrations.AlterField(
            model_name='joblist',
            name='pid',
            field=models.IntegerField(help_text='', null=True, verbose_name='Pid'),
        ),
        migrations.AlterField(
            model_name='joblist',
            name='servername',
            field=models.CharField(help_text='', max_length=35, verbose_name='Servername'),
        ),
        migrations.AlterField(
            model_name='joblist',
            name='status',
            field=models.CharField(blank=True, help_text='', max_length=35, null=True, verbose_name='Status'),
        ),
    ]