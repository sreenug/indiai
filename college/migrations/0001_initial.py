# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Leadership'
        db.create_table(u'college_leadership', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name_company', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('name_founder', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('year_trust', self.gf('django.db.models.fields.IntegerField')(max_length=4)),
            ('month_college', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('year_college', self.gf('django.db.models.fields.IntegerField')(max_length=4)),
        ))
        db.send_create_signal(u'college', ['Leadership'])

        # Adding model 'Recognition'
        db.create_table(u'college_recognition', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('course_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('type_approval', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('easyness', self.gf('django.db.models.fields.TextField')()),
            ('criteria', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'college', ['Recognition'])

        # Adding model 'Accreditation'
        db.create_table(u'college_accreditation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year_rating', self.gf('django.db.models.fields.IntegerField')(max_length=4)),
            ('rating', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('rating_body', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'college', ['Accreditation'])

        # Adding model 'Award'
        db.create_table(u'college_award', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name_award', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('awarding_body', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('year_award', self.gf('django.db.models.fields.IntegerField')(max_length=4)),
        ))
        db.send_create_signal(u'college', ['Award'])

        # Adding model 'College'
        db.create_table(u'college_college', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('street_address_1', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('street_address_2', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('pincode', self.gf('django.db.models.fields.IntegerField')(max_length=6, null=True, blank=True)),
            ('latitude', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=31, decimal_places=28, blank=True)),
            ('longitude', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=32, decimal_places=28, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('telephone', self.gf('django.db.models.fields.CharField')(max_length=12)),
            ('principal_name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('principal_number', self.gf('django.db.models.fields.CharField')(max_length=12)),
            ('respondent_name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('respondent_designation', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('college_accreditated', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('campus_size', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('builtup_area', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('distance_railway', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('distance_bus', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('number_labs', self.gf('django.db.models.fields.IntegerField')(max_length=3)),
            ('boys_hostel', self.gf('django.db.models.fields.FloatField')(max_length=5)),
            ('girls_hostel', self.gf('django.db.models.fields.FloatField')(max_length=5)),
            ('playground', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('number_sport_centers', self.gf('django.db.models.fields.IntegerField')(max_length=3)),
            ('transport_facility', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('number_buses', self.gf('django.db.models.fields.IntegerField')(max_length=3)),
            ('number_mini_buses', self.gf('django.db.models.fields.IntegerField')(max_length=3)),
        ))
        db.send_create_signal(u'college', ['College'])

        # Adding M2M table for field leaderships on 'College'
        db.create_table(u'college_college_leaderships', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('college', models.ForeignKey(orm[u'college.college'], null=False)),
            ('leadership', models.ForeignKey(orm[u'college.leadership'], null=False))
        ))
        db.create_unique(u'college_college_leaderships', ['college_id', 'leadership_id'])

        # Adding M2M table for field recognition on 'College'
        db.create_table(u'college_college_recognition', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('college', models.ForeignKey(orm[u'college.college'], null=False)),
            ('recognition', models.ForeignKey(orm[u'college.recognition'], null=False))
        ))
        db.create_unique(u'college_college_recognition', ['college_id', 'recognition_id'])

        # Adding M2M table for field accreditations on 'College'
        db.create_table(u'college_college_accreditations', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('college', models.ForeignKey(orm[u'college.college'], null=False)),
            ('accreditation', models.ForeignKey(orm[u'college.accreditation'], null=False))
        ))
        db.create_unique(u'college_college_accreditations', ['college_id', 'accreditation_id'])

        # Adding M2M table for field awards on 'College'
        db.create_table(u'college_college_awards', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('college', models.ForeignKey(orm[u'college.college'], null=False)),
            ('award', models.ForeignKey(orm[u'college.award'], null=False))
        ))
        db.create_unique(u'college_college_awards', ['college_id', 'award_id'])


    def backwards(self, orm):
        # Deleting model 'Leadership'
        db.delete_table(u'college_leadership')

        # Deleting model 'Recognition'
        db.delete_table(u'college_recognition')

        # Deleting model 'Accreditation'
        db.delete_table(u'college_accreditation')

        # Deleting model 'Award'
        db.delete_table(u'college_award')

        # Deleting model 'College'
        db.delete_table(u'college_college')

        # Removing M2M table for field leaderships on 'College'
        db.delete_table('college_college_leaderships')

        # Removing M2M table for field recognition on 'College'
        db.delete_table('college_college_recognition')

        # Removing M2M table for field accreditations on 'College'
        db.delete_table('college_college_accreditations')

        # Removing M2M table for field awards on 'College'
        db.delete_table('college_college_awards')


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