# Generated by Django 3.0.3 on 2020-02-23 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0002_vwo'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entity', models.CharField(max_length=200)),
                ('program', models.CharField(max_length=200)),
                ('target', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
                ('website', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='VWO',
        ),
    ]
