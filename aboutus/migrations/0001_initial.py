# Generated by Django 5.1.4 on 2025-01-05 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
            ],
            options={
                'verbose_name': 'about us ',
                'verbose_name_plural': 'about us ',
            },
        ),
        migrations.CreateModel(
            name='Chef',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('bio', models.TextField()),
                ('image', models.ImageField(upload_to='chef/')),
            ],
            options={
                'verbose_name': 'chef',
                'verbose_name_plural': 'chef',
            },
        ),
        migrations.CreateModel(
            name='Why_Choose_Us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
            ],
            options={
                'verbose_name': 'why choose us ',
                'verbose_name_plural': 'why choose us ',
            },
        ),
    ]
