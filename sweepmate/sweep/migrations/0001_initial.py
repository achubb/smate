# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Backer'
        db.create_table(u'sweep_backer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('firstname', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('lastname', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
        ))
        db.send_create_signal(u'sweep', ['Backer'])

        # Adding model 'Event'
        db.create_table(u'sweep_event', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('eventname', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('eventdesc', self.gf('django.db.models.fields.TextField')()),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
        ))
        db.send_create_signal(u'sweep', ['Event'])

        # Adding model 'Sweep'
        db.create_table(u'sweep_sweep', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sweepname', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('sweepevent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sweep.Event'])),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
        ))
        db.send_create_signal(u'sweep', ['Sweep'])

        # Adding model 'Player'
        db.create_table(u'sweep_player', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('playername', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('playersweep', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sweep.Sweep'])),
            ('playerbacker', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sweep.Backer'])),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
        ))
        db.send_create_signal(u'sweep', ['Player'])


    def backwards(self, orm):
        # Deleting model 'Backer'
        db.delete_table(u'sweep_backer')

        # Deleting model 'Event'
        db.delete_table(u'sweep_event')

        # Deleting model 'Sweep'
        db.delete_table(u'sweep_sweep')

        # Deleting model 'Player'
        db.delete_table(u'sweep_player')


    models = {
        u'sweep.backer': {
            'Meta': {'object_name': 'Backer'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'sweep.event': {
            'Meta': {'object_name': 'Event'},
            'eventdesc': ('django.db.models.fields.TextField', [], {}),
            'eventname': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'sweep.player': {
            'Meta': {'object_name': 'Player'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'playerbacker': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sweep.Backer']"}),
            'playername': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'playersweep': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sweep.Sweep']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'sweep.sweep': {
            'Meta': {'object_name': 'Sweep'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'sweepevent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sweep.Event']"}),
            'sweepname': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['sweep']