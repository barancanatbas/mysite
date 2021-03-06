# Generated by Django 3.1.1 on 2020-10-11 14:57

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_remove_post_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='bilgilendirme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resim', models.ImageField(blank=True, null=True, upload_to='', verbose_name='tanıtım resim')),
                ('yazi', ckeditor_uploader.fields.RichTextUploadingField()),
                ('telefon', models.CharField(max_length=12, null=True)),
                ('email', models.CharField(max_length=30, null=True)),
                ('instagram', models.CharField(max_length=200, null=True)),
                ('facebook', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='reports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
            ],
        ),
    ]
