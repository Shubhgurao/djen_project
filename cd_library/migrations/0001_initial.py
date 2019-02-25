# Generated by Django 2.1.3 on 2019-02-21 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('artist', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('genre', models.CharField(choices=[('R', 'Rock'), ('B', 'Blue'), ('J', 'Jazz'), ('P', 'Pop')], max_length=1)),
            ],
        ),
    ]
