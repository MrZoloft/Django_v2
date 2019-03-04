# Generated by Django 2.1.1 on 2019-03-04 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0002_auto_20190228_1800'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=235)),
                ('url', models.URLField(blank=True)),
                ('text', models.TextField()),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=True, to='blog.Post')),
            ],
        ),
    ]