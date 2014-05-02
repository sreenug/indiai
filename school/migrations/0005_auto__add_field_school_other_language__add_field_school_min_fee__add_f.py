# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'School.other_language'
        db.add_column(u'school_school', 'other_language',
                      self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True),
                      keep_default=False)

        # Adding field 'School.min_fee'
        db.add_column(u'school_school', 'min_fee',
                      self.gf('django.db.models.fields.IntegerField')(max_length=6, null=True, blank=True),
                      keep_default=False)

        # Adding field 'School.max_fee'
        db.add_column(u'school_school', 'max_fee',
                      self.gf('django.db.models.fields.IntegerField')(max_length=6, null=True, blank=True),
                      keep_default=False)

        # Adding field 'School.establishment'
        db.add_column(u'school_school', 'establishment',
                      self.gf('django.db.models.fields.IntegerField')(default=0, max_length=4),
                      keep_default=False)

        # Adding field 'School.recognition'
        db.add_column(u'school_school', 'recognition',
                      self.gf('django.db.models.fields.IntegerField')(default=0, max_length=4),
                      keep_default=False)


        # Changing field 'School.street_address_1'
        db.alter_column(u'school_school', 'street_address_1', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'School.street_address_2'
        db.alter_column(u'school_school', 'street_address_2', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))
        # Adding unique constraint on 'School', fields ['pincode', 'street_address_1', 'name', 'street_address_2']
        db.create_unique(u'school_school', ['pincode', 'street_address_1', 'name', 'street_address_2'])


    def backwards(self, orm):
        # Removing unique constraint on 'School', fields ['pincode', 'street_address_1', 'name', 'street_address_2']
        db.delete_unique(u'school_school', ['pincode', 'street_address_1', 'name', 'street_address_2'])

        # Deleting field 'School.other_language'
        db.delete_column(u'school_school', 'other_language')

        # Deleting field 'School.min_fee'
        db.delete_column(u'school_school', 'min_fee')

        # Deleting field 'School.max_fee'
        db.delete_column(u'school_school', 'max_fee')

        # Deleting field 'School.establishment'
        db.delete_column(u'school_school', 'establishment')

        # Deleting field 'School.recognition'
        db.delete_column(u'school_school', 'recognition')


        # Changing field 'School.street_address_1'
        db.alter_column(u'school_school', 'street_address_1', self.gf('django.db.models.fields.CharField')(max_length=500, null=True))

        # Changing field 'School.street_address_2'
        db.alter_column(u'school_school', 'street_address_2', self.gf('django.db.models.fields.CharField')(max_length=500, null=True))

    models = {
        u'school.school': {
            'Meta': {'unique_together': "(('name', 'street_address_1', 'street_address_2', 'pincode'),)", 'object_name': 'School'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'establishment': ('django.db.models.fields.IntegerField', [], {'max_length': '4'}),
            'highest_class': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '31', 'decimal_places': '28', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '32', 'decimal_places': '28', 'blank': 'True'}),
            'lowest_class': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'management_type': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'max_fee': ('django.db.models.fields.IntegerField', [], {'max_length': '6', 'null': 'True', 'blank': 'True'}),
            'medium_of_instruction': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'min_fee': ('django.db.models.fields.IntegerField', [], {'max_length': '6', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'other_language': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'pincode': ('django.db.models.fields.IntegerField', [], {'max_length': '6', 'null': 'True', 'blank': 'True'}),
            'recognition': ('django.db.models.fields.IntegerField', [], {'max_length': '4'}),
            'recognized': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'street_address_1': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'street_address_2': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['school']