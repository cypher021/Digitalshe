# Generated by Django 4.0.6 on 2022-07-17 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendes',
            name='training_location',
            field=models.CharField(choices=[('Kathmandu', 'Kathmandu'), ('Dolakha', 'Dolakha'), ('Lalitpur', 'Lalitpur'), ('Teku', 'Teku'), ('Bhaktapur', 'Bhaktapur'), ('Hetauda', 'Hetauda')], default='Kathmandu', max_length=30),
        ),
    ]
