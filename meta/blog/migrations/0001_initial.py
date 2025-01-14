# Generated by Django 4.2.3 on 2025-01-08 10:46

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('title', models.CharField(default=0, max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('demo_link', models.CharField(blank=True, max_length=200, null=True)),
                ('source_link', models.CharField(blank=True, max_length=200, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.IntegerField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]
