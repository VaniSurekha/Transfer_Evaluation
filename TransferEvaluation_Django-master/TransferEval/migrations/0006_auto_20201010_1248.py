# Generated by Django 3.1.2 on 2020-10-10 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TransferEval', '0005_auto_20201010_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='approver',
            name='approver_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
