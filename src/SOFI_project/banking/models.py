from django.db import models
import datetime
import decimal




class LegalPerson(models.Model):
    name = models.CharField(max_length=256, unique=True)
    code = models.IntegerField(unique=True)
    address = models.CharField(max_length=256)
    
    def pay_salary(self):
        for lp_account in self.legalpersonaccount_set.all():
            for employment in lp_account.employment_set.all():
                try:
                    salary = employment.legal_person_account.account.withdraw(employment.salary)
                    tax_total_sum = 0
                    for tax in employment.taxes.all():
                        tax_sum = tax.part * salary
                        tax_total_sum += tax_sum
                        tax.government_unit.account.deposit(tax_sum)
                    employment.natural_person_account.account.deposit(salary - tax_total_sum)
                except:
                    raise
    
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
    

class Account(models.Model):
    __balance = models.DecimalField(max_digits=12, decimal_places=2)
    __rate = models.DecimalField(max_digits=10, decimal_places=6)
    __last_transaction_time = models.DateTimeField()
    
    def __recalculate_balance(self):
        def total_microseconds(td):
            return td.microseconds + (td.seconds + td.days * 24 * 3600) * 10**6
        year = datetime.timedelta(days=365)
        now = datetime.datetime.now()
        delta = decimal.Decimal(total_microseconds(now  - self.__last_transaction_time))
        years_part = delta / decimal.Decimal(total_microseconds(year))
        total_power = years_part * self.__rate
        self.__balance *= total_power.exp()
        self.__balance = self.__balance.quantize(decimal.Decimal('0.01'))
        self.__last_transaction_time = now
        self.save()
        
    
    def withdraw(self, sum_of_money):
        if sum_of_money <= decimal.Decimal('0.01'):
            raise Exception('The sum of money to withdraw must be positive')
        self.__recalculate_balance()
        if sum_of_money > self.__balance:
            raise Exception('Not enough money on account')
        self.__balance -= sum_of_money
        self.save()
        return sum_of_money
    
    def deposit(self, sum_of_money):
        if sum_of_money <= decimal.Decimal('0.01'):
            raise Exception('The sum of money to deposit must be positive')
        self.__recalculate_balance()
        self.__balance += sum_of_money
        self.save()
        return self.balance
    
    def get_balance(self):
        self.__recalculate_balance()
        return self.__balance
    
    def get_rate(self):
        return self.__rate
    
    balance = property(get_balance)
    rate = property(get_rate)
    
    def __unicode__(self):
        return u'%d' % self.id
    

class LegalPersonAccount(models.Model):
    account = models.OneToOneField(Account)
    legal_person = models.ForeignKey(LegalPerson)
    
    def __unicode__(self):
        return u'%s - %s' % (self.legal_person, self.account.balance)
    
    
class NaturalPersonAccount(models.Model):
    account = models.OneToOneField(Account)
    natural_person = models.ForeignKey(NaturalPerson)
    
    def __unicode__(self):
        return u'%s - %s' % (self.natural_person, self.account.balance)

class GovernmentUnit(models.Model):
    name = models.CharField(max_length=256)
    account = models.OneToOneField(Account)
    
    def __unicode__(self):
        return u'%s - %s' % (self.name, self.account.balance)


class Tax(models.Model):
    government_unit = models.ForeignKey(GovernmentUnit)
    part = models.DecimalField(max_digits=10, decimal_places=6)
    name = models.CharField(max_length=256)
    
    class Meta:
        verbose_name_plural = "taxes"
    
    def __unicode__(self):
        return u'%s - %s - %s' % (self.name, self.government_unit, self.part)


class Employment(models.Model):
    natural_person_account = models.ForeignKey(NaturalPersonAccount)
    legal_person_account = models.ForeignKey(LegalPersonAccount)
    salary = models.DecimalField(max_digits=12, decimal_places=2)
    taxes = models.ManyToManyField(Tax)
    
    def __unicode__(self):
        return u'%s - %s - %s' % (self.natural_person_account.natural_person, self.legal_person_account.legal_person, self.salary)