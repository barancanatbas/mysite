# Generated by Django 3.1.1 on 2020-09-27 16:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Kategori',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kategoriad', models.CharField(max_length=250, verbose_name='kategoriad')),
            ],
        ),
        migrations.CreateModel(
            name='SiteSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SiteTitle', models.CharField(max_length=200, verbose_name='Site Başlığı')),
                ('SiteMainTitle', models.CharField(max_length=300, null=True, verbose_name='site ana başlık')),
                ('SiteImage', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Site Fotoğrafı')),
                ('SiteDescription', models.TextField(verbose_name='Site Açıklama')),
                ('SiteChangeDate', models.DateTimeField(auto_now_add=True, verbose_name='değiştirme zamanı ')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='başlık')),
                ('content', models.TextField(verbose_name='içerik')),
                ('publising_date', models.DateTimeField(auto_now_add=True, verbose_name='yayınlanma tarihi')),
                ('image', models.ImageField(default='resim.png', upload_to='')),
                ('kategori', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.kategori', verbose_name='kategori')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL, verbose_name='yazar')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='İsim')),
                ('comment', models.TextField(verbose_name='yorum')),
                ('comment_date_time', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='post.post', verbose_name='post')),
            ],
        ),
    ]
