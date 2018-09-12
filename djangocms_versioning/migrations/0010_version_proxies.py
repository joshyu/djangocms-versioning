# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-30 22:38
from __future__ import unicode_literals

from django.apps import apps
from django.db import migrations


def make_operations():
    versioning_extension = apps.get_app_config('djangocms_versioning').cms_extension

    return [
        migrations.CreateModel(
            name=versionable.version_model_proxy.__name__,
            fields=[
            ],
            options={
                'managed': False,
                'proxy': True,
            },
            bases=('djangocms_versioning.version',),
        ) for versionable in versioning_extension.versionables
    ]


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_versioning', '0009_cms_pagecontent_remove_unique_constraint'),
    ]

    operations = make_operations()