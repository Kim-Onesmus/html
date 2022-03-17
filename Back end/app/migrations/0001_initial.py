# Generated by Django 4.0.3 on 2022-03-16 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(default=None, max_length=200)),
                ('username', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update', models.DateField(auto_now=True)),
                ('category', models.CharField(choices=[('food', 'food'), ('clothing', 'clothing'), ('electronics', 'electronics'), ('vehicles', 'vehicles'), ('cyber', 'cyber'), ('supermarket', 'supermarket'), ('fruits_vegetables', 'fruits_vegetables'), ('hardware', 'hardware')], max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='media/')),
                ('delivery', models.CharField(choices=[('free delivery', 'free delivery'), ('no delivery', 'no delivery')], max_length=200)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
    ]
