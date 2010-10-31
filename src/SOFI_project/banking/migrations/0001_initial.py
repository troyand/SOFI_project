# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'LegalPerson'
        db.create_table('banking_legalperson', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal('banking', ['LegalPerson'])

        # Adding model 'NaturalPerson'
        db.create_table('banking_naturalperson', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('surname', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('state_personal_id', self.gf('django.db.models.fields.IntegerField')()),
            ('works_for', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['banking.LegalPerson'])),
        ))
        db.send_create_signal('banking', ['NaturalPerson'])


    def backwards(self, orm):
        
        # Deleting model 'LegalPerson'
        db.delete_table('banking_legalperson')

        # Deleting model 'NaturalPerson'
        db.delete_table('banking_naturalperson')


    models = {
        'banking.legalperson': {
            'Meta': {'object_name': 'LegalPerson'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'banking.naturalperson': {
            'Meta': {'object_name': 'NaturalPerson'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'state_personal_id': ('django.db.models.fields.IntegerField', [], {}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'works_for': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['banking.LegalPerson']"})
        }
    }

    complete_apps = ['banking']
