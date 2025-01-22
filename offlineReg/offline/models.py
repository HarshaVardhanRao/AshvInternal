from django.db import models
from datetime import datetime

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Event(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="events")
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Registration(models.Model):
    sec_choices = [
        ('A','A'),('B','B'),('C','C'),('D','D'),('E','E'),('F','F'),('G','G'),('H','H'),('I','I'),('J','J')
    ]
    dept_choices = [
        ('CSE','CSE'),('CAI','CAI'),('CSD','CSD'),('CSM','CSM'),('CSN','CSN'),('CSC','CSC'),('CST','CST'),('ECE','ECE'),('EEE','EEE'),('MECH','MECH'),('CIVIL','CIVIL'),('MBA','MBA'),('MCA','MCA'),('MTECH','MTECH')
    ]
    year_choices = [
        (1,1),(2,2),(3,3),(4,4)
    ]
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20)
    year = models.IntegerField(choices=year_choices,default=1)
    branch = models.CharField(max_length=50,choices=dept_choices,default='CSE')
    section = models.CharField(max_length=10,choices=sec_choices,default='A')
    email = models.EmailField()
    mobile_number = models.CharField(max_length=15)
    payment_recived = models.CharField(max_length=100,default='Mr. V. Mustafa',null=True,blank=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    registered_on = models.DateField(default=datetime.now)
