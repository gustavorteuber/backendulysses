# Generated by Django 4.1.5 on 2023-01-20 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0001_initial'),
        ('core', '0005_empreendimentos_local'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='banner',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='uploader.image'),
        ),
    ]