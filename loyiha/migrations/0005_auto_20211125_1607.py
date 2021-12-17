# Generated by Django 3.2.9 on 2021-11-25 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loyiha', '0004_alter_loyiha_talaba'),
    ]

    operations = [
        migrations.CreateModel(
            name='Eng_yaxshi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('darajasi', models.CharField(max_length=100)),
                ('loyihasi', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='talabalar',
            name='otasi_ismi',
        ),
        migrations.RemoveField(
            model_name='talabalar',
            name='qachon_oqigan',
        ),
        migrations.AddField(
            model_name='talabalar',
            name='darajasi',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='talabalar',
            name='holati',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='talabalar',
            name='malumoti',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='talabalar',
            name='familiyasi',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='talabalar',
            name='ismi',
            field=models.CharField(max_length=1000),
        ),
    ]