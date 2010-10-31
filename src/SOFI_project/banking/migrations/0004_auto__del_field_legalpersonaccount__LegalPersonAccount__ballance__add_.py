# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'LegalPersonAccount._LegalPersonAccount__ballance'
        db.delete_column('banking_legalpersonaccount', '_LegalPersonAccount__ballance')

        # Adding field 'LegalPersonAccount._LegalPersonAccount__balance'
        db.add_column('banking_legalpersonaccount', '_LegalPersonAccount__balance', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=12, decimal_places=2), keep_default=False)


    def backwards(self, orm):
        
        # Adding field 'LegalPersonAccount._LegalPersonAccount__ballance'
        db.add_column('banking_legalpersonaccount', '_LegalPersonAccount__ballance', self.gf('django.db.models.fields.DecimalField')(default=1, max_digits=12, decimal_places=2), keep_default=False)

        # Deleting field 'LegalPersonAccount._LegalPersonAccount__balance'
        db.delete_column('banking_legalpersonaccount', '_LegalPersonAccount__balance')


    models = {
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
        }
    }

    complete_apps = ['banking']
