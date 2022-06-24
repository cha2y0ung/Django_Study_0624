# Generated by Django 4.0.5 on 2022-06-24 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('content', models.CharField(max_length=200)),
                ('is_done', models.BooleanField(default=False)),
            ],
        ),
    ]
