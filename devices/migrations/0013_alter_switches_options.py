# Generated by Django 4.1.7 on 2023-06-02 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0012_alter_device_type_of_device'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='switches',
            options={'verbose_name': 'Przełącznik', 'verbose_name_plural': 'Przełączniki'},
        ),
    ]