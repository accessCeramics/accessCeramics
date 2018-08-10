# Generated by Django 2.0.7 on 2018-08-10 20:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('given_name', models.CharField(help_text='100 characters maximum.', max_length=100)),
                ('family_name', models.CharField(help_text='100 characters maximum.', max_length=100)),
                ('additional_name', models.CharField(blank=True, help_text='100 characters maximum.', max_length=100, null=True)),
                ('birth_year', models.PositiveSmallIntegerField(blank=True, help_text='YYYY format.', null=True)),
                ('death_year', models.PositiveSmallIntegerField(blank=True, help_text='YYYY format.', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='people.Person')),
                ('statement', models.TextField(blank=True, null=True)),
                ('bio', models.TextField(blank=True, null=True)),
            ],
            bases=('people.person',),
        ),
    ]
