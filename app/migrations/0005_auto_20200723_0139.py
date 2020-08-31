# Generated by Django 3.0.2 on 2020-07-22 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20200723_0100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('S', 'Sports'), ('H', 'Health & Beauty'), ('B', 'Books'), ('MF', 'Men Fashion'), ('WF', 'Women Fashion'), ('PH', 'Phones & Tablets'), ('K', 'Kids & Babies'), ('L', 'Laptops & PCs')], max_length=2),
        ),
        migrations.AlterField(
            model_name='item',
            name='label',
            field=models.CharField(choices=[('A', ''), ('P', 'primary'), ('S', 'secondary'), ('D', 'danger')], max_length=1),
        ),
    ]