# Generated by Django 2.1.3 on 2018-11-30 04:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('linkworld', '0002_auto_20181130_0249'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='approved_comment',
        ),
    ]
