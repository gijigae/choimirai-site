# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields
import wagtail.wagtailcore.blocks
import wagtail.wagtailembeds.blocks
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('rca', '0020_auto_20151112_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rcablogpage',
            name='streamfield',
            field=wagtail.wagtailcore.fields.StreamField([(b'h2', wagtail.wagtailcore.blocks.CharBlock(classname=b'title', icon=b'title')), (b'h3', wagtail.wagtailcore.blocks.CharBlock(classname=b'title', icon=b'title')), (b'h4', wagtail.wagtailcore.blocks.CharBlock(classname=b'title', icon=b'title')), (b'intro', wagtail.wagtailcore.blocks.RichTextBlock(icon=b'pilcrow')), (b'paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon=b'pilcrow')), (b'bustout', wagtail.wagtailcore.blocks.StructBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock()), (b'text', wagtail.wagtailcore.blocks.RichTextBlock())])), (b'pullquote', wagtail.wagtailcore.blocks.StructBlock([(b'quote', wagtail.wagtailcore.blocks.CharBlock(classname=b'quote title')), (b'attribution', wagtail.wagtailcore.blocks.CharBlock())])), (b'raw_html', wagtail.wagtailcore.blocks.RawHTMLBlock(icon=b'code', label=b'Raw HTML')), (b'embed', wagtail.wagtailembeds.blocks.EmbedBlock(icon=b'code'))], blank=True),
        ),
    ]
