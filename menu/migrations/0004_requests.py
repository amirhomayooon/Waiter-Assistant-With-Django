# Generated by Django 4.1 on 2022-08-18 08:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_alter_item_price_alter_item_thumbnail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Requests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('desk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.desk')),
            ],
        ),
    ]
