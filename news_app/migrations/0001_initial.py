# Generated by Django 4.2.1 on 2023-05-25 07:01

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250)),
                ('body', models.TextField()),
                ('image', models.ImageField(upload_to='news/image')),
                ('publish_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('DF', 'Draft'), ('PB', 'Published')], default='DF', max_length=2)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news_app.category')),
            ],
            options={
                'ordering': ['-publish_time'],
            },
        ),
    ]
