# Generated by Django 2.2.6 on 2019-11-04 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adm', '0002_eventlst_pointstable'),
    ]

    operations = [
        migrations.AddField(
            model_name='pointstable',
            name='medals',
            field=models.CharField(default='0', max_length=20),
        ),
    ]
