# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'School.teacher_strength'
        db.add_column(u'school_school', 'teacher_strength',
                      self.gf('django.db.models.fields.IntegerField')(max_length=10, null=True, blank=True),
                      keep_default=False)

        # Adding field 'School.student_strength'
        db.add_column(u'school_school', 'student_strength',
                      self.gf('django.db.models.fields.IntegerField')(max_length=10, null=True, blank=True),
                      keep_default=False)

        # Adding field 'School.email'
        db.add_column(u'school_school', 'email',
                      self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True),
                      keep_default=False)

        # Adding field 'School.phone_number'
        db.add_column(u'school_school', 'phone_number',
                      self.gf('django.db.models.fields.IntegerField')(max_length=12, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'School.teacher_strength'
        db.delete_column(u'school_school', 'teacher_strength')

        # Deleting field 'School.student_strength'
        db.delete_column(u'school_school', 'student_strength')

        # Deleting field 'School.email'
        db.delete_column(u'school_school', 'email')

        # Deleting field 'School.phone_number'
        db.delete_column(u'school_school', 'phone_number')


    models = {
        u'school.school': {
            'Meta': {'unique_together': "(('name', 'street_address_1', 'street_address_2', 'pincode'),)", 'object_name': 'School'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
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
            'phone_number': ('django.db.models.fields.IntegerField', [], {'max_length': '12', 'null': 'True', 'blank': 'True'}),
            'pincode': ('django.db.models.fields.IntegerField', [], {'max_length': '6', 'null': 'True', 'blank': 'True'}),
            'recognition': ('django.db.models.fields.IntegerField', [], {'max_length': '4'}),
            'recognized': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'street_address_1': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'street_address_2': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'student_strength': ('django.db.models.fields.IntegerField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'teacher_strength': ('django.db.models.fields.IntegerField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['school']