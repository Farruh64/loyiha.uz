# Generated by Django 3.2.9 on 2021-11-24 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loyiha', '0003_auto_20211124_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loyiha',
            name='talaba',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loyihalar', to='loyiha.talabalar'),
        ),
    ]
