# Generated by Django 3.0.3 on 2023-03-31 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=10)),
                ('profile', models.ImageField(null=True, upload_to='pics')),
                ('hall', models.IntegerField(null=True)),
            ],
        ),
    ]
