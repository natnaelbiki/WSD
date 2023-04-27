from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
POSITION_DATA = [('manager',"Manager"),('customer service manager',"Customer Service Manager"),
	('operation manager',"Operation Manager"),('digital officer',"Digital Officer"),('internal control manager',"Internal Control Manager"),
	('business manager',"Business Manager"),]
BRANCH_DATA = [('wolaita sodo', "Wolaita Sodo"), ('otona', "Otona"), ('kawo sana', 'Kawo Sana')]
class Branch(models.Model):
        name = models.CharField(max_length=50, choices=BRANCH_DATA, blank=False, unique=True)
        phone_regex = RegexValidator(regex=r'^\+?251?\d{9}$', message="Phone number incorrect. it should start +251 format")
        phone = models.CharField(validators=[phone_regex], max_length=13, default='04xxxxxxxx')
        phone1 = models.CharField(validators=[phone_regex], max_length=13, blank=True, default='')
        phone2 = models.CharField(validators=[phone_regex], max_length=13, blank=True, default='')
        phone3 = models.CharField(validators=[phone_regex], max_length=13, blank=True, default='')
        phone4 = models.CharField(validators=[phone_regex], max_length=13, blank=True, default='')

        def __str__(self):
                return self.name

class Manager(models.Model):
        name = models.CharField(max_length=50, blank=False, unique=True, db_index=True)
        branch = models.CharField(max_length=50, choices=BRANCH_DATA, blank=False)
        position = models.CharField(max_length=100, choices=POSITION_DATA, default="Manager")
        mphone_regex = RegexValidator(regex=r'^\+?251?\d{9}$', message="Phone number incorrect. it should start +251 format")
        m_phone = models.CharField(validators=[mphone_regex], max_length=13, default='04xxxxxxxx')
        m_phone1 = models.CharField(validators=[mphone_regex], max_length=13, blank=True, default='')
        m_phone2 = models.CharField(validators=[mphone_regex], max_length=13, blank=True, default='')
        m_phone3 = models.CharField(validators=[mphone_regex], max_length=13, blank=True, default='')

        def __str__(self):
                return self.name

STATUS = [('pending','Pending'),('on progress','on Progress'),('done',"Done")]

class Ticket(models.Model):
        t_id = models.IntegerField(blank=False, unique=True)
        name = models.CharField(max_length=50, blank=False)
        case = models.CharField(max_length=50, blank=False)
        date = models.DateTimeField(auto_now=True)
        status = models.CharField(max_length=20, choices=STATUS)