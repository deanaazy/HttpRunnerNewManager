# Generated by Django 2.0.3 on 2020-06-01 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ApiManager', '0002_sshinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sshinfo',
            name='port',
            field=models.IntegerField(default=22, null=True),
        ),
    ]
