# Generated by Django 2.2.9 on 2020-03-16 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('setting_name', models.CharField(max_length=100)),
                ('setting_value', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['-setting_name'],
            },
        ),
    ]
