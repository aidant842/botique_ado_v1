# Generated by Django 3.0.7 on 2020-07-02 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_auto_20200629_1551'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='origonal_bag',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='order',
            name='stripe_pid',
            field=models.CharField(default='', max_length=254),
        ),
    ]