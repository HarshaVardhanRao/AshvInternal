from django.db import models

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
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20)
    year = models.IntegerField()
    branch = models.CharField(max_length=50,choices=dept_choices,default='CSE')
    section = models.CharField(max_length=10,choices=sec_choices,default='A')
    email = models.EmailField()
    mobile_number = models.CharField(max_length=15)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    registered_on = models.DateField(auto_now_add=True)
