# Generated by Django 4.2.3 on 2025-01-09 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_project_featured_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='featured_image',
            field=models.ImageField(blank=True, default='Sking.jpg', null=True, upload_to=''),
        ),
    ]
