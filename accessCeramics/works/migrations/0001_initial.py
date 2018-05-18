# Generated by Django 2.0.4 on 2018-04-13 19:29

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Technique',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='An artistic technique used in the making of a work.', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='The title of the work. Max 500 characters.', max_length=500, verbose_name='title')),
                ('description', models.TextField(help_text='A short description of the work.', null=True, verbose_name='description')),
                ('creators', models.ManyToManyField(help_text='accessCeramics user(s) who created the work.', to=settings.AUTH_USER_MODEL)),
                ('materials', models.ManyToManyField(help_text='Materials used to make the work.', to='works.Material')),
                ('techniques', models.ManyToManyField(help_text='Artistic techniques used to make the work.', to='works.Technique')),
            ],
        ),
        migrations.CreateModel(
            name='WorkType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='work',
            name='work_types',
            field=models.ManyToManyField(help_text='Types or functions of the work, e.g. "vase".', to='works.WorkType'),
        ),
    ]