# Generated by Django 3.2.12 on 2022-02-24 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(blank=True, max_length=50, null=True)),
                ('contact', models.IntegerField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.ImageField(blank=True, default='profiles/user-default.png', null=True, upload_to='profiles/')),
            ],
        ),
    ]
