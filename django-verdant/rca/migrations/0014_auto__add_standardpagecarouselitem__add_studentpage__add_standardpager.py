# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'StandardPageCarouselItem'
        db.create_table(u'rca_standardpagecarouselitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('page', self.gf('django.db.models.fields.related.ForeignKey')(related_name='carousel_items', to=orm['rca.StandardPage'])),
            ('image', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['verdantimages.Image'])),
            ('embedly_url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
        ))
        db.send_create_signal(u'rca', ['StandardPageCarouselItem'])

        # Adding model 'StudentPage'
        db.create_table(u'rca_studentpage', (
            (u'page_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.Page'], unique=True, primary_key=True)),
            ('social_image', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['verdantimages.Image'])),
            ('social_text', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'rca', ['StudentPage'])

        # Adding model 'StandardPageRelatedLink'
        db.create_table(u'rca_standardpagerelatedlink', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('page', self.gf('django.db.models.fields.related.ForeignKey')(related_name='related_links', to=orm['rca.StandardPage'])),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('link_text', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'rca', ['StandardPageRelatedLink'])

        # Adding model 'JobPage'
        db.create_table(u'rca_jobpage', (
            (u'page_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.Page'], unique=True, primary_key=True)),
            ('social_image', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['verdantimages.Image'])),
            ('social_text', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'rca', ['JobPage'])

        # Adding model 'ResearchInnovationPage'
        db.create_table(u'rca_researchinnovationpage', (
            (u'page_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.Page'], unique=True, primary_key=True)),
            ('social_image', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['verdantimages.Image'])),
            ('social_text', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'rca', ['ResearchInnovationPage'])

        # Adding model 'HomePage'
        db.create_table(u'rca_homepage', (
            (u'page_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.Page'], unique=True, primary_key=True)),
            ('social_image', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['verdantimages.Image'])),
            ('social_text', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'rca', ['HomePage'])

        # Adding model 'ResearchItem'
        db.create_table(u'rca_researchitem', (
            (u'page_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.Page'], unique=True, primary_key=True)),
            ('social_image', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['verdantimages.Image'])),
            ('social_text', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'rca', ['ResearchItem'])

        # Adding model 'ContactUsPage'
        db.create_table(u'rca_contactuspage', (
            (u'page_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.Page'], unique=True, primary_key=True)),
            ('social_image', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['verdantimages.Image'])),
            ('social_text', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'rca', ['ContactUsPage'])

        # Adding model 'StandardPage'
        db.create_table(u'rca_standardpage', (
            (u'page_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.Page'], unique=True, primary_key=True)),
            ('social_image', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['verdantimages.Image'])),
            ('social_text', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('intro', self.gf('core.fields.RichTextField')(blank=True)),
            ('body', self.gf('core.fields.RichTextField')(blank=True)),
        ))
        db.send_create_signal(u'rca', ['StandardPage'])

        # Adding model 'StandardIndex'
        db.create_table(u'rca_standardindex', (
            (u'page_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.Page'], unique=True, primary_key=True)),
            ('social_image', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['verdantimages.Image'])),
            ('social_text', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'rca', ['StandardIndex'])

        # Adding model 'JobsIndex'
        db.create_table(u'rca_jobsindex', (
            (u'page_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.Page'], unique=True, primary_key=True)),
            ('social_image', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['verdantimages.Image'])),
            ('social_text', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'rca', ['JobsIndex'])

        # Adding model 'GalleryPage'
        db.create_table(u'rca_gallerypage', (
            (u'page_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.Page'], unique=True, primary_key=True)),
            ('social_image', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['verdantimages.Image'])),
            ('social_text', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'rca', ['GalleryPage'])

        # Adding model 'RcaNowPage'
        db.create_table(u'rca_rcanowpage', (
            (u'page_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.Page'], unique=True, primary_key=True)),
            ('social_image', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['verdantimages.Image'])),
            ('social_text', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'rca', ['RcaNowPage'])

        # Adding model 'CurrentResearchPage'
        db.create_table(u'rca_currentresearchpage', (
            (u'page_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.Page'], unique=True, primary_key=True)),
            ('social_image', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['verdantimages.Image'])),
            ('social_text', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'rca', ['CurrentResearchPage'])

        # Adding model 'StaffPage'
        db.create_table(u'rca_staffpage', (
            (u'page_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.Page'], unique=True, primary_key=True)),
            ('social_image', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['verdantimages.Image'])),
            ('social_text', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'rca', ['StaffPage'])

        # Adding model 'RcaNowIndex'
        db.create_table(u'rca_rcanowindex', (
            (u'page_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.Page'], unique=True, primary_key=True)),
            ('social_image', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['verdantimages.Image'])),
            ('social_text', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'rca', ['RcaNowIndex'])


    def backwards(self, orm):
        # Deleting model 'StandardPageCarouselItem'
        db.delete_table(u'rca_standardpagecarouselitem')

        # Deleting model 'StudentPage'
        db.delete_table(u'rca_studentpage')

        # Deleting model 'StandardPageRelatedLink'
        db.delete_table(u'rca_standardpagerelatedlink')

        # Deleting model 'JobPage'
        db.delete_table(u'rca_jobpage')

        # Deleting model 'ResearchInnovationPage'
        db.delete_table(u'rca_researchinnovationpage')

        # Deleting model 'HomePage'
        db.delete_table(u'rca_homepage')

        # Deleting model 'ResearchItem'
        db.delete_table(u'rca_researchitem')

        # Deleting model 'ContactUsPage'
        db.delete_table(u'rca_contactuspage')

        # Deleting model 'StandardPage'
        db.delete_table(u'rca_standardpage')

        # Deleting model 'StandardIndex'
        db.delete_table(u'rca_standardindex')

        # Deleting model 'JobsIndex'
        db.delete_table(u'rca_jobsindex')

        # Deleting model 'GalleryPage'
        db.delete_table(u'rca_gallerypage')

        # Deleting model 'RcaNowPage'
        db.delete_table(u'rca_rcanowpage')

        # Deleting model 'CurrentResearchPage'
        db.delete_table(u'rca_currentresearchpage')

        # Deleting model 'StaffPage'
        db.delete_table(u'rca_staffpage')

        # Deleting model 'RcaNowIndex'
        db.delete_table(u'rca_rcanowindex')


    models = {
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'core.page': {
            'Meta': {'object_name': 'Page'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'pages'", 'to': u"orm['contenttypes.ContentType']"}),
            'depth': ('django.db.models.fields.PositiveIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numchild': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'path': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'rca.authorpage': {
            'Meta': {'object_name': 'AuthorPage', '_ormbases': [u'rca.EditorialPage']},
            u'editorialpage_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['rca.EditorialPage']", 'unique': 'True', 'primary_key': 'True'}),
            'mugshot': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['verdantimages.Image']"})
        },
        u'rca.authorsindex': {
            'Meta': {'object_name': 'AuthorsIndex', '_ormbases': [u'core.Page']},
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.Page']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'rca.contactuspage': {
            'Meta': {'object_name': 'ContactUsPage', '_ormbases': [u'core.Page']},
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'social_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['verdantimages.Image']"}),
            'social_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'rca.currentresearchpage': {
            'Meta': {'object_name': 'CurrentResearchPage', '_ormbases': [u'core.Page']},
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'social_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['verdantimages.Image']"}),
            'social_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'rca.editorialpage': {
            'Meta': {'object_name': 'EditorialPage', '_ormbases': [u'core.Page']},
            'body': ('core.fields.RichTextField', [], {}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.Page']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'rca.eventitem': {
            'Meta': {'object_name': 'EventItem', '_ormbases': [u'core.Page']},
            'audience': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'cost': ('core.fields.RichTextField', [], {'blank': 'True'}),
            'date_from': ('django.db.models.fields.DateField', [], {}),
            'date_to': ('django.db.models.fields.DateField', [], {}),
            'gallery': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'listing_intro': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'related_programme': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'event_item'", 'null': 'True', 'to': u"orm['rca.ProgrammePage']"}),
            'related_school': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'event_item'", 'null': 'True', 'to': u"orm['rca.SchoolPage']"}),
            'show_on_homepage': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'signup_link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'social_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['verdantimages.Image']"}),
            'social_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'specific_directions': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'specific_directions_link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'times': ('core.fields.RichTextField', [], {'blank': 'True'})
        },
        u'rca.eventitemcarouselitem': {
            'Meta': {'object_name': 'EventItemCarouselItem'},
            'embedly_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['verdantimages.Image']"}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'carousel_items'", 'to': u"orm['rca.EventItem']"})
        },
        u'rca.eventitemspeaker': {
            'Meta': {'object_name': 'EventItemSpeaker'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['verdantimages.Image']"}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'speakers'", 'to': u"orm['rca.EventItem']"}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'rca.gallerypage': {
            'Meta': {'object_name': 'GalleryPage', '_ormbases': [u'core.Page']},
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'social_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['verdantimages.Image']"}),
            'social_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'rca.homepage': {
            'Meta': {'object_name': 'HomePage', '_ormbases': [u'core.Page']},
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'social_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['verdantimages.Image']"}),
            'social_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'rca.jobpage': {
            'Meta': {'object_name': 'JobPage', '_ormbases': [u'core.Page']},
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'social_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['verdantimages.Image']"}),
            'social_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'rca.jobsindex': {
            'Meta': {'object_name': 'JobsIndex', '_ormbases': [u'core.Page']},
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'social_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['verdantimages.Image']"}),
            'social_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'rca.newsindex': {
            'Meta': {'object_name': 'NewsIndex', '_ormbases': [u'core.Page']},
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.Page']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'rca.newsitem': {
            'Meta': {'object_name': 'NewsItem', '_ormbases': [u'core.Page']},
            'area': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'author': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'news_items'", 'null': 'True', 'to': u"orm['rca.AuthorPage']"}),
            'body': ('core.fields.RichTextField', [], {}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'listing_intro': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'related_programme': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'news_item'", 'null': 'True', 'to': u"orm['rca.ProgrammePage']"}),
            'related_school': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'news_item'", 'null': 'True', 'to': u"orm['rca.SchoolPage']"}),
            'show_on_homepage': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'social_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['verdantimages.Image']"}),
            'social_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'rca.newsitemcarouselitem': {
            'Meta': {'object_name': 'NewsItemCarouselItem'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['verdantimages.Image']"}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'carousel_items'", 'to': u"orm['rca.NewsItem']"}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'rca.newsitemrelatedlink': {
            'Meta': {'object_name': 'NewsItemRelatedLink'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link_text': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'related_links'", 'to': u"orm['rca.NewsItem']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'rca.programmepage': {
            'Meta': {'object_name': 'ProgrammePage', '_ormbases': [u'core.Page']},
            'download_document_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'download_document_url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'head_of_programme': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'head_of_programme_statement': ('core.fields.RichTextField', [], {}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'programme_video': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'rca.programmepagecarouselitem': {
            'Meta': {'object_name': 'ProgrammePageCarouselItem'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['verdantimages.Image']"}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'carousel_items'", 'to': u"orm['rca.ProgrammePage']"}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'rca.programmepagefacilities': {
            'Meta': {'object_name': 'ProgrammePageFacilities'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['verdantimages.Image']"}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'facilities'", 'to': u"orm['rca.ProgrammePage']"}),
            'text': ('core.fields.RichTextField', [], {})
        },
        u'rca.programmepageoursites': {
            'Meta': {'object_name': 'ProgrammePageOurSites'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['verdantimages.Image']"}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'our_sites'", 'to': u"orm['rca.ProgrammePage']"}),
            'site_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'rca.programmepagerelatedlink': {
            'Meta': {'object_name': 'ProgrammePageRelatedLink'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link_text': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'related_links'", 'to': u"orm['rca.ProgrammePage']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'rca.programmepagestudentstory': {
            'Meta': {'object_name': 'ProgrammePageStudentStory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['verdantimages.Image']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'student_stories'", 'to': u"orm['rca.ProgrammePage']"}),
            'text': ('core.fields.RichTextField', [], {})
        },
        u'rca.rcanowindex': {
            'Meta': {'object_name': 'RcaNowIndex', '_ormbases': [u'core.Page']},
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'social_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['verdantimages.Image']"}),
            'social_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'rca.rcanowpage': {
            'Meta': {'object_name': 'RcaNowPage', '_ormbases': [u'core.Page']},
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'social_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['verdantimages.Image']"}),
            'social_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'rca.relateddocument': {
            'Meta': {'object_name': 'RelatedDocument'},
            'document': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['verdantdocs.Document']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'related_documents'", 'to': u"orm['core.Page']"})
        },
        u'rca.relatedlink': {
            'Meta': {'object_name': 'RelatedLink'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['verdantimages.Image']"}),
            'link_text': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'generic_related_links'", 'to': u"orm['core.Page']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'rca.researchinnovationpage': {
            'Meta': {'object_name': 'ResearchInnovationPage', '_ormbases': [u'core.Page']},
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'social_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['verdantimages.Image']"}),
            'social_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'rca.researchitem': {
            'Meta': {'object_name': 'ResearchItem', '_ormbases': [u'core.Page']},
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'social_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['verdantimages.Image']"}),
            'social_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'rca.schoolpage': {
            'Meta': {'object_name': 'SchoolPage', '_ormbases': [u'core.Page']},
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.Page']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'rca.staffpage': {
            'Meta': {'object_name': 'StaffPage', '_ormbases': [u'core.Page']},
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'social_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['verdantimages.Image']"}),
            'social_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'rca.standardindex': {
            'Meta': {'object_name': 'StandardIndex', '_ormbases': [u'core.Page']},
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'social_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['verdantimages.Image']"}),
            'social_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'rca.standardpage': {
            'Meta': {'object_name': 'StandardPage', '_ormbases': [u'core.Page']},
            'body': ('core.fields.RichTextField', [], {'blank': 'True'}),
            'intro': ('core.fields.RichTextField', [], {'blank': 'True'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'social_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['verdantimages.Image']"}),
            'social_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'rca.standardpagecarouselitem': {
            'Meta': {'object_name': 'StandardPageCarouselItem'},
            'embedly_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['verdantimages.Image']"}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'carousel_items'", 'to': u"orm['rca.StandardPage']"})
        },
        u'rca.standardpagerelatedlink': {
            'Meta': {'object_name': 'StandardPageRelatedLink'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link_text': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'related_links'", 'to': u"orm['rca.StandardPage']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'rca.studentpage': {
            'Meta': {'object_name': 'StudentPage', '_ormbases': [u'core.Page']},
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'social_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['verdantimages.Image']"}),
            'social_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'taggit.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'})
        },
        u'taggit.taggeditem': {
            'Meta': {'object_name': 'TaggedItem'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'taggit_taggeditem_tagged_items'", 'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'taggit_taggeditem_items'", 'to': u"orm['taggit.Tag']"})
        },
        u'verdantdocs.document': {
            'Meta': {'object_name': 'Document'},
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'verdantimages.image': {
            'Meta': {'object_name': 'Image'},
            'file': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'height': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'width': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['rca']