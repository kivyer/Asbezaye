# Generated by Django 4.0.3 on 2022-05-27 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0002_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=100)),
                ('amount', models.IntegerField(max_length=100)),
                ('unit', models.CharField(max_length=5)),
                ('for_when', models.DateTimeField(verbose_name='when to deliver')),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App1.user')),
            ],
        ),
    ]
