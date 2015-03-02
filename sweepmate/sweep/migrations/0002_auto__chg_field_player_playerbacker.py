# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Player.playerbacker'
        db.alter_column(u'sweep_player', 'playerbacker_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sweep.Backer'], null=True))

    def backwards(self, orm):

        # Changing field 'Player.playerbacker'
        db.alter_column(u'sweep_player', 'playerbacker_id', self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['sweep.Backer']))

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
            'playerbacker': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sweep.Backer']", 'null': 'True'}),
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