# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'GalleryItem.type'
        db.delete_column(u'gallery_galleryitem', 'type')

        # Adding field 'GalleryItem.project'
        db.add_column(u'gallery_galleryitem', 'project',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gallery.Project'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'GalleryItem.type'
        db.add_column(u'gallery_galleryitem', 'type',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=100),
                      keep_default=False)

        # Deleting field 'GalleryItem.project'
        db.delete_column(u'gallery_galleryitem', 'project_id')


    models = {
        u'gallery.galleryitem': {
            'Meta': {'object_name': 'GalleryItem'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['gallery.Project']", 'null': 'True', 'blank': 'True'})
        },
        u'gallery.project': {
            'Meta': {'object_name': 'Project'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['gallery']