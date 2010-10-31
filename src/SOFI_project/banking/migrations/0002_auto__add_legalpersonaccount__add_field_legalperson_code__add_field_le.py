# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'LegalPersonAccount'
        db.create_table('banking_legalpersonaccount', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('_LegalPersonAccount__ballance', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=2)),
            ('_LegalPersonAccount__rate', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=6)),
            ('_LegalPersonAccount__last_transaction_time', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('banking', ['LegalPersonAccount'])

        # Adding field 'LegalPerson.code'
        db.add_column('banking_legalperson', 'code', self.gf('django.db.models.fields.IntegerField')(default=1), keep_default=False)

        # Adding field 'LegalPerson.address'
        db.add_column('banking_legalperson', 'address', self.gf('django.db.models.fields.CharField')(default='', max_length=256), keep_default=False)

        # Deleting field 'NaturalPerson.works_for'
        db.delete_column('banking_naturalperson', 'works_for_id')

        # Deleting field 'NaturalPerson.state_personal_id'
        db.delete_column('banking_naturalperson', 'state_personal_id')

        # Adding field 'NaturalPerson.personal_id'
        db.add_column('banking_naturalperson', 'personal_id', self.gf('django.db.models.fields.IntegerField')(default=1), keep_default=False)


    def backwards(self, orm):
        
        # Deleting model 'LegalPersonAccount'
        db.delete_table('banking_legalpersonaccount')

        # Deleting field 'LegalPerson.code'
        db.delete_column('banking_legalperson', 'code')

        # Deleting field 'LegalPerson.address'
        db.delete_column('banking_legalperson', 'address')

        # Adding field 'NaturalPerson.works_for'
        db.add_column('banking_naturalperson', 'works_for', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['banking.LegalPerson']), keep_default=False)

        # Adding field 'NaturalPerson.state_personal_id'
        db.add_column('banking_naturalperson', 'state_personal_id', self.gf('django.db.models.fields.IntegerField')(default=1), keep_default=False)

        # Deleting field 'NaturalPerson.personal_id'
        db.delete_column('banking_naturalperson', 'personal_id')


    models = {
        'banking.legalperson': {
            'Meta': {'object_name': 'LegalPerson'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'code': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'banking.legalpersonaccount': {
            'Meta': {'object_name': 'LegalPersonAccount'},
            '_LegalPersonAccount__ballance': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '2'}),
            '_LegalPersonAccount__last_transaction_time': ('django.db.models.fields.DateTimeField', [], {}),
            '_LegalPersonAccount__rate': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '6'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'banking.naturalperson': {
            'Meta': {'object_name': 'NaturalPerson'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'personal_id': ('django.db.models.fields.IntegerField', [], {}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        }
    }

    complete_apps = ['banking']
