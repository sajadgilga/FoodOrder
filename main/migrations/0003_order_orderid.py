# Generated by Django 2.1.3 on 2018-11-21 08:44

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='orderID',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
