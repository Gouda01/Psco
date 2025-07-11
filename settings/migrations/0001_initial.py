# Generated by Django 4.2 on 2025-07-04 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Management',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('code', models.CharField(max_length=35, unique=True)),
                ('details', models.TextField(blank=True, max_length=5000, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('edited_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'permissions': [('add_settings', 'Can add settings'), ('change_settings', 'Can change settings'), ('view_settings', 'Can view settings'), ('delete_settings', 'Can delete settings')],
            },
        ),
    ]
