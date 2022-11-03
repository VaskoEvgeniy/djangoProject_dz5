# Generated by Django 4.1.3 on 2022-11-03 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=32)),
                ('category_slug', models.SlugField(max_length=32)),
                ('category_description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
