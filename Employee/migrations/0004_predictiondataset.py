# Generated by Django 4.0.3 on 2022-03-27 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0003_auto_20220118_2029'),
    ]

    operations = [
        migrations.CreateModel(
            name='PredictionDataSet',
            fields=[
                ('id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='Employee.employee')),
                ('satisfaction_level', models.FloatField(blank=True, null=True)),
                ('last_evaluation', models.IntegerField(blank=True, null=True)),
                ('salary', models.CharField(blank=True, max_length=50, null=True)),
                ('department', models.CharField(blank=True, max_length=50, null=True)),
                ('number_project', models.IntegerField(blank=True, null=True)),
                ('average_montly_hours', models.IntegerField(blank=True, null=True)),
                ('time_spend_company', models.IntegerField(blank=True, null=True)),
                ('Work_accident', models.IntegerField(blank=True, null=True)),
                ('promotion_last_5years', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]