from django.db import models



# Create your models here.

class LegalPerson(models.Model):
    name = models.CharField(max_length=256, unique=True)
    code = models.IntegerField(unique=True)
    address = models.CharField(max_length=256)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "legal people"



class NaturalPerson(models.Model):
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    personal_id = models.IntegerField(unique=True)
    
    def __unicode__(self):
        return '%s %s' % (self.name, self.surname)
    
    class Meta:
        verbose_name_plural = "natural people"
    

class LegalPersonAccount(models.Model):
    __balance = models.DecimalField(max_digits=12, decimal_places=2)
    __rate = models.DecimalField(max_digits=10, decimal_places=6)
    __last_transaction_time = models.DateTimeField()
    legal_person = models.ForeignKey(LegalPerson)
    
    def get_balance(self):
        return self.__balance
    
    def get_rate(self):
        return self.__rate
    
    balance = property(get_balance)
    rate = property(get_rate)
    
    
class NaturalPersonAccount(models.Model):
    __balance = models.DecimalField(max_digits=12, decimal_places=2)
    __rate = models.DecimalField(max_digits=10, decimal_places=6)
    __last_transaction_time = models.DateTimeField()
    natural_person = models.ForeignKey(NaturalPerson)
    
    def get_balance(self):
        return self.__balance
    
    def withdraw(self, sum_of_money):
        if sum_of_money <= 0:
            raise Exception('The sum of money to withdraw must be positive')
        #TODO recalculate balance with percents
        if sum_of_money > self.__balance:
            raise Exception('Not enough money on account')
        self.__balance -= sum_of_money
        self.save()
        return sum_of_money
    
    def deposit(self, sum_of_money):
        if sum_of_money <= 0:
            raise Exception('The sum of money to deposit must be positive')
        #TODO recalculate balance with percents
        self.__balance += sum_of_money
        self.save()
        return self.balance
    
    def get_rate(self):
        return self.__rate
    
    balance = property(get_balance)
    rate = property(get_rate)
    
class Employment(models.Model):
    natural_person_account = models.ForeignKey(NaturalPersonAccount)
    legal_person_account = models.ForeignKey(LegalPersonAccount)
    salary = models.DecimalField(max_digits=12, decimal_places=2)