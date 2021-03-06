# Generated by Django 3.0.1 on 2019-12-28 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pytsm', '0010_auto_20191229_0023'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cfgmainmenu',
            old_name='CFG_PYTSM_LABEL',
            new_name='cfg_pytsm_base_label',
        ),
        migrations.RenameField(
            model_name='cfgmainmenu',
            old_name='CFG_PYTSM_NAME',
            new_name='cfg_pytsm_base_name',
        ),
        migrations.RenameField(
            model_name='cfgmainmenu',
            old_name='CFG_PYTSM_SORTORDER',
            new_name='cfg_pytsm_base_sortorder',
        ),
        migrations.RenameField(
            model_name='cfgoverview',
            old_name='alert_cmp',
            new_name='cfg_pytsm_base_alert_cmp',
        ),
        migrations.RenameField(
            model_name='cfgoverview',
            old_name='alert_col',
            new_name='cfg_pytsm_base_alert_col',
        ),
        migrations.RenameField(
            model_name='cfgoverview',
            old_name='alert_val',
            new_name='cfg_pytsm_base_alert_val',
        ),
        migrations.RenameField(
            model_name='cfgoverview',
            old_name='CFG_PYTSM_LABEL',
            new_name='cfg_pytsm_base_label',
        ),
        migrations.RenameField(
            model_name='cfgoverview',
            old_name='CFG_PYTSM_NAME',
            new_name='cfg_pytsm_base_name',
        ),
        migrations.RenameField(
            model_name='cfgoverview',
            old_name='CFG_PYTSM_SORTORDER',
            new_name='cfg_pytsm_base_sortorder',
        ),
        migrations.RenameField(
            model_name='cfgoverviewbox',
            old_name='CFG_PYTSM_LABEL',
            new_name='cfg_pytsm_base_label',
        ),
        migrations.RenameField(
            model_name='cfgoverviewbox',
            old_name='CFG_PYTSM_NAME',
            new_name='cfg_pytsm_base_name',
        ),
        migrations.RenameField(
            model_name='cfgoverviewbox',
            old_name='CFG_PYTSM_SORTORDER',
            new_name='cfg_pytsm_base_sortorder',
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
        migrations.AlterField(
            model_name='logpolldstat',
            name='enabled',
            field=models.BooleanField(default=True, help_text='', verbose_name='Enabled'),
        ),
        migrations.AlterField(
            model_name='logpolldstat',
            name='lastrun',
            field=models.DateTimeField(help_text='', verbose_name='Lastrun'),
        ),
        migrations.AlterField(
            model_name='logpolldstat',
            name='nextrun',
            field=models.DateTimeField(help_text='', verbose_name='Nextrun'),
        ),
        migrations.AlterField(
            model_name='logpolldstat',
            name='status',
            field=models.CharField(blank=True, help_text='', max_length=35, null=True, verbose_name='Status'),
        ),
    ]
