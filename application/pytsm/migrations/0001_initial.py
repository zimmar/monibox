# Generated by Django 3.0.1 on 2019-12-26 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CfgColors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the color', max_length=35, verbose_name='Name')),
                ('value', models.CharField(help_text='H_CFG_COLOR_VALUE', max_length=7, verbose_name='Value')),
            ],
            options={
                'verbose_name': 'Color',
                'verbose_name_plural': 'Colors',
                'db_table': 'cfg_colors',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='CfgConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('confkey', models.CharField(help_text='H_CFG_CONFIG_KEY', max_length=35, verbose_name='Config Key')),
                ('confval', models.CharField(help_text='H_CFG_CONFIG_VALUE', max_length=255, verbose_name='Config Value')),
                ('description', models.CharField(help_text='H_CFG_CONFIG_DESCRIPTION', max_length=255, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Config',
                'verbose_name_plural': 'Configs',
                'db_table': 'cfg_config',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='CfgMainmenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35, verbose_name='Name')),
                ('label', models.CharField(max_length=35, verbose_name='Label')),
                ('sortorder', models.SmallIntegerField(verbose_name='Sort Order')),
            ],
            options={
                'verbose_name': 'Mainmenu',
                'verbose_name_plural': 'Mainmenues',
                'db_table': 'cfg_mainmenu',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='CfgOverviewbox',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Overviewbox',
                'verbose_name_plural': 'Overviewboxes',
                'db_table': 'cfg_overviewbox',
            },
        ),
        migrations.CreateModel(
            name='CfgServer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servername', models.CharField(db_index=True, help_text='H_CFG_SRV_SERVERNAME', max_length=35, verbose_name='Servername')),
                ('instanzname', models.CharField(default='tsminst1', help_text='H_CFG_SRV_INSTANZNAME', max_length=35, verbose_name='Instanzname')),
                ('description', models.CharField(help_text='H_CFG_SRV_DESCRIPTION', max_length=35, null=True, verbose_name='Description')),
                ('ip', models.CharField(help_text='H_CFG_SRV_TCPIP', max_length=15, verbose_name='IP')),
                ('port', models.PositiveSmallIntegerField(default=1500, help_text='H_CFG_SRV_PORT', verbose_name='Port')),
                ('username', models.CharField(help_text='H_CFG_SRV_USERNAME', max_length=35, verbose_name='Username')),
                ('password', models.CharField(help_text='H_CFG_SRV_PASSWORD', max_length=35, verbose_name='Password')),
                ('libraryclient', models.BooleanField(default=False, help_text='H_CFG_SRV_LIBRARYCLIENT', verbose_name='Libraryclient')),
                ('default', models.BooleanField(default=False, help_text='H_CFG_SRV_DEFAULT', verbose_name='Default')),
                ('checks', models.BooleanField(default=True, help_text='H_CFG_SRV_CHECK', verbose_name='Run Queries')),
            ],
            options={
                'verbose_name': 'Server',
                'verbose_name_plural': 'Servers',
                'db_table': 'cfg_server',
                'unique_together': {('servername', 'instanzname', 'port')},
            },
        ),
    ]
