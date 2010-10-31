# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding unique constraint on 'LegalPerson', fields ['code']
        db.create_unique('banking_legalperson', ['code'])

        # Adding unique constraint on 'LegalPerson', fields ['name']
        db.create_unique('banking_legalperson', ['name'])

        # Adding unique constraint on 'NaturalPerson', fields ['personal_id']
        db.create_unique('banking_naturalperson', ['personal_id'])

        # Adding field 'LegalPersonAccount.legal_person'
        db.add_column('banking_legalpersonaccount', 'legal_person', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['banking.LegalPerson']), keep_default=False)


    def backwards(self, orm):
        
        # Removing unique constraint on 'NaturalPerson', fields ['personal_id']
        db.delete_unique('banking_naturalperson', ['personal_id'])

        # Removing unique constraint on 'LegalPerson', fields ['name']
        db.delete_unique('banking_legalperson', ['name'])

        # Removing unique constraint on 'LegalPerson', fields ['code']
        db.delete_unique('banking_legalperson', ['code'])

        # Deleting field 'LegalPersonAccount.legal_person'
        db.delete_column('banking_legalpersonaccount', 'legal_person_id')


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
            '_LegalPersonAccount__ballance': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '2'}),
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
