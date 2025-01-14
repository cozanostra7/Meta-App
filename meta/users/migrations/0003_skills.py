# Generated by Django 4.2.3 on 2025-01-14 07:12

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('owner', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.profile')),
            ],
        ),
    ]
