# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-02 08:04
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
        ('hbd', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AlterField(
            model_name='birthday',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='hbd.User'),
        ),
        migrations.AlterField(
            model_name='cheers',
            name='pals',
            field=models.ManyToManyField(related_name='cheers_made', to='hbd.User'),
        ),
        migrations.AlterField(
            model_name='cheers',
            name='target_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cheers_to', to='hbd.User'),
        ),
    ]
