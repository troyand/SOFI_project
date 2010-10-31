# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Employment'
        db.create_table('banking_employment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('natural_person_account', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['banking.NaturalPersonAccount'])),
            ('legal_person_account', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['banking.LegalPersonAccount'])),
            ('salary', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=2)),
        ))
        db.send_create_signal('banking', ['Employment'])

        # Adding model 'NaturalPersonAccount'
        db.create_table('banking_naturalpersonaccount', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('_NaturalPersonAccount__balance', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=2)),
            ('_NaturalPersonAccount__rate', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=6)),
            ('_NaturalPersonAccount__last_transaction_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('natural_person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['banking.NaturalPerson'])),
        ))
        db.send_create_signal('banking', ['NaturalPersonAccount'])


    def backwards(self, orm):
        
        # Deleting model 'Employment'
        db.delete_table('banking_employment')

        # Deleting model 'NaturalPersonAccount'
        db.delete_table('banking_naturalpersonaccount')


    models = {
        'banking.employment': {
            'Meta': {'object_name': 'Employment'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'legal_person_account': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['banking.LegalPersonAccount']"}),
            'natural_person_account': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['banking.NaturalPersonAccount']"}),
            'salary': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '2'})
        },
        'banking.legalperson': {
            'Meta': {'object_name': 'LegalPerson'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'code': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '256'})
        },
        'banking.legalpersonaccount': {
            'Meta': {'object_name': 'LegalPersonAccount'},
            '_LegalPersonAccount__balance': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '2'}),
            '_LegalPersonAccount__last_transaction_time': ('django.db.models.fields.DateTimeField', [], {}),
            '_LegalPersonAccount__rate': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '6'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'legal_person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['banking.LegalPerson']"})
        },
        'banking.naturalperson': {
            'Meta': {'object_name': 'NaturalPerson'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'personal_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        'banking.naturalpersonaccount': {
            'Meta': {'object_name': 'NaturalPersonAccount'},
            '_NaturalPersonAccount__balance': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '2'}),
            '_NaturalPersonAccount__last_transaction_time': ('django.db.models.fields.DateTimeField', [], {}),
            '_NaturalPersonAccount__rate': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '6'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'natural_person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['banking.NaturalPerson']"})
        }
    }

    complete_apps = ['banking']
