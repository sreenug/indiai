# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'School.street_address_1'
        db.add_column(u'school_school', 'street_address_1',
                      self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True),
                      keep_default=False)

        # Adding field 'School.street_address_2'
        db.add_column(u'school_school', 'street_address_2',
                      self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True),
                      keep_default=False)

        # Adding field 'School.city'
        db.add_column(u'school_school', 'city',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'School.state'
        db.add_column(u'school_school', 'state',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'School.pincode'
        db.add_column(u'school_school', 'pincode',
                      self.gf('django.db.models.fields.IntegerField')(max_length=6, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'School.street_address_1'
        db.delete_column(u'school_school', 'street_address_1')

        # Deleting field 'School.street_address_2'
        db.delete_column(u'school_school', 'street_address_2')

        # Deleting field 'School.city'
        db.delete_column(u'school_school', 'city')

        # Deleting field 'School.state'
        db.delete_column(u'school_school', 'state')

        # Deleting field 'School.pincode'
        db.delete_column(u'school_school', 'pincode')


    models = {
        u'school.school': {
            'Meta': {'object_name': 'School'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'highest_class': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '31', 'decimal_places': '28', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '32', 'decimal_places': '28', 'blank': 'True'}),
            'lowest_class': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'management_type': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'medium_of_instruction': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'pincode': ('django.db.models.fields.IntegerField', [], {'max_length': '6', 'null': 'True', 'blank': 'True'}),
            'recognized': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'street_address_1': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'street_address_2': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['school']