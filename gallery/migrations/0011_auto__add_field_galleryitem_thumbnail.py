# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Project.year'
        db.alter_column(u'gallery_project', 'year', self.gf('django.db.models.fields.IntegerField')(null=True))
        # Adding field 'GalleryItem.media_type'
        db.add_column(u'gallery_galleryitem', 'media_type',
                      self.gf('django.db.models.fields.CharField')(default='Image', max_length=20),
                      keep_default=False)

        # Adding field 'GalleryItem.thumbnail'
        db.add_column(u'gallery_galleryitem', 'thumbnail',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'GalleryItem.video_embed_code'
        db.add_column(u'gallery_galleryitem', 'video_embed_code',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):

        # Changing field 'Project.year'
        db.alter_column(u'gallery_project', 'year', self.gf('django.db.models.fields.IntegerField')(default='Image'))
        # Deleting field 'GalleryItem.media_type'
        db.delete_column(u'gallery_galleryitem', 'media_type')

        # Deleting field 'GalleryItem.thumbnail'
        db.delete_column(u'gallery_galleryitem', 'thumbnail')

        # Deleting field 'GalleryItem.video_embed_code'
        db.delete_column(u'gallery_galleryitem', 'video_embed_code')


    models = {
        u'gallery.galleryitem': {
            'Meta': {'object_name': 'GalleryItem'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'media_type': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['gallery.Project']", 'null': 'True', 'blank': 'True'}),
            'thumbnail': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'video_embed_code': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'gallery.project': {
            'Meta': {'object_name': 'Project'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['gallery']