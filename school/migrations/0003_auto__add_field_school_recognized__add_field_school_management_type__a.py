# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'School.recognized'
        db.add_column(u'school_school', 'recognized',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=10),
                      keep_default=False)

        # Adding field 'School.management_type'
        db.add_column(u'school_school', 'management_type',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=100),
                      keep_default=False)

        # Adding field 'School.medium_of_instruction'
        db.add_column(u'school_school', 'medium_of_instruction',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'School.recognized'
        db.delete_column(u'school_school', 'recognized')

        # Deleting field 'School.management_type'
        db.delete_column(u'school_school', 'management_type')

        # Deleting field 'School.medium_of_instruction'
        db.delete_column(u'school_school', 'medium_of_instruction')


    models = {
        u'school.school': {
            'Meta': {'object_name': 'School'},
            'highest_class': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '31', 'decimal_places': '28', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '32', 'decimal_places': '28', 'blank': 'True'}),
            'lowest_class': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'management_type': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'medium_of_instruction': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'recognized': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        }
    }

    complete_apps = ['school']