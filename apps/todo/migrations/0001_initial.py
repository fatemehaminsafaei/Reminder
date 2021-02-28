# Generated by Django 3.1.7 on 2021-02-24 14:42

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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Name')),
                ('slug', models.SlugField(max_length=100, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, unique=True, verbose_name='Title')),
                ('slug', models.SlugField(verbose_name='Slug')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('priority', models.CharField(choices=[('V-Imp', '!!!'), ('Imp', '!!'), ('N-V-Imp', '!'), ('N-Imp', 'None')], max_length=7, verbose_name='Priority')),
                ('due_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('done', models.BooleanField(default=False, verbose_name='Done')),
                ('category', models.ForeignKey(default='general', on_delete=django.db.models.deletion.PROTECT, to='todo.category')),
            ],
            options={
                'ordering': ['due_date'],
            },
        ),
    ]