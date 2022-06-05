# Generated by Django 4.0.3 on 2022-06-01 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0007_comments'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comments',
            new_name='CommentsP',
        ),
        migrations.CreateModel(
            name='CommentsB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=1000)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App1.user')),
            ],
        ),
    ]
