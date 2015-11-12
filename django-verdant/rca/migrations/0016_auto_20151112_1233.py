# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rca', '0015_merge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactsnippetemail',
            name='page',
        ),
        migrations.RemoveField(
            model_name='contactsnippetphone',
            name='page',
        ),
        migrations.RemoveField(
            model_name='contactsnippetplacement',
            name='contact_snippet',
        ),
        migrations.RemoveField(
            model_name='contactsnippetplacement',
            name='page',
        ),
        migrations.RemoveField(
            model_name='customcontentmoduleblock',
            name='content_module',
        ),
        migrations.RemoveField(
            model_name='customcontentmoduleblock',
            name='image',
        ),
        migrations.RemoveField(
            model_name='customcontentmoduleblock',
            name='link',
        ),
        migrations.RemoveField(
            model_name='customecontentmoduleplacement',
            name='custom_content_module',
        ),
        migrations.RemoveField(
            model_name='customecontentmoduleplacement',
            name='page',
        ),
        migrations.RemoveField(
            model_name='standardindexcontactsnippet',
            name='contact_snippet',
        ),
        migrations.RemoveField(
            model_name='standardindexcontactsnippet',
            name='page',
        ),
        migrations.RemoveField(
            model_name='standardindexcustomcontentmodules',
            name='custom_content_module',
        ),
        migrations.RemoveField(
            model_name='standardindexcustomcontentmodules',
            name='page',
        ),
        migrations.DeleteModel(
            name='ContactSnippet',
        ),
        migrations.DeleteModel(
            name='ContactSnippetEmail',
        ),
        migrations.DeleteModel(
            name='ContactSnippetPhone',
        ),
        migrations.DeleteModel(
            name='ContactSnippetPlacement',
        ),
        migrations.DeleteModel(
            name='CustomContentModule',
        ),
        migrations.DeleteModel(
            name='CustomContentModuleBlock',
        ),
        migrations.DeleteModel(
            name='CustomeContentModulePlacement',
        ),
        migrations.DeleteModel(
            name='StandardIndexContactSnippet',
        ),
        migrations.DeleteModel(
            name='StandardIndexCustomContentModules',
        ),
    ]
