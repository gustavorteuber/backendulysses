# Generated by Django 4.1.5 on 2023-01-24 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0001_initial'),
        ('core', '0012_rename_publicacao_dolar_indice'),
    ]

    operations = [
        migrations.CreateModel(
            name='acoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('link', models.TextField()),
                ('foto', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='uploader.image')),
            ],
        ),
    ]
