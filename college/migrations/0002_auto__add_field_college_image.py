# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'College.image'
        db.add_column(u'college_college', 'image',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'College.image'
        db.delete_column(u'college_college', 'image')


    models = {
        u'college.accreditation': {
            'Meta': {'object_name': 'Accreditation'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rating': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'rating_body': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'year_rating': ('django.db.models.fields.IntegerField', [], {'max_length': '4'})
        },
        u'college.award': {
            'Meta': {'object_name': 'Award'},
            'awarding_body': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_award': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'year_award': ('django.db.models.fields.IntegerField', [], {'max_length': '4'})
        },
        u'college.college': {
            'Meta': {'object_name': 'College'},
            'accreditations': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['college.Accreditation']", 'symmetrical': 'False'}),
            'awards': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['college.Award']", 'symmetrical': 'False'}),
            'boys_hostel': ('django.db.models.fields.FloatField', [], {'max_length': '5'}),
            'builtup_area': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'campus_size': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'college_accreditated': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'distance_bus': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'distance_railway': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'girls_hostel': ('django.db.models.fields.FloatField', [], {'max_length': '5'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '31', 'decimal_places': '28', 'blank': 'True'}),
            'leaderships': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['college.Leadership']", 'symmetrical': 'False'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '32', 'decimal_places': '28', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'number_buses': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'number_labs': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'number_mini_buses': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'number_sport_centers': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'pincode': ('django.db.models.fields.IntegerField', [], {'max_length': '6', 'null': 'True', 'blank': 'True'}),
            'playground': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'principal_name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'principal_number': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'recognition': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['college.Recognition']", 'symmetrical': 'False'}),
            'respondent_designation': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'respondent_name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'street_address_1': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'street_address_2': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'transport_facility': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'college.leadership': {
            'Meta': {'object_name': 'Leadership'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'month_college': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'name_company': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name_founder': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'year_college': ('django.db.models.fields.IntegerField', [], {'max_length': '4'}),
            'year_trust': ('django.db.models.fields.IntegerField', [], {'max_length': '4'})
        },
        u'college.recognition': {
            'Meta': {'object_name': 'Recognition'},
            'course_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'criteria': ('django.db.models.fields.TextField', [], {}),
            'easyness': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type_approval': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['college']