# Generated by Django 4.2 on 2024-05-03 00:59

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contactform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Contactform_uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('customer_name', models.CharField(max_length=50)),
                ('customer_email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
    ]