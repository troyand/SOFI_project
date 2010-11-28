from banking.models import *
from django.contrib import admin

admin.site.register(LegalPerson)
admin.site.register(NaturalPerson)
admin.site.register(Account)
admin.site.register(LegalPersonAccount)
admin.site.register(NaturalPersonAccount)
admin.site.register(Employment)
admin.site.register(GovernmentUnit)
admin.site.register(Tax)