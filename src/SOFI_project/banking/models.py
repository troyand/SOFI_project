from django.db import models



# Create your models here.

class LegalPerson(models.Model):
    name = models.CharField(max_length=256)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "legal people"



class NaturalPerson(models.Model):
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    state_personal_id = models.IntegerField()
    works_for = models.ForeignKey(LegalPerson)
    
    def __unicode__(self):
        return '%s %s' % (self.name, self.surname)
    
    class Meta:
        verbose_name_plural = "natural people"
    

