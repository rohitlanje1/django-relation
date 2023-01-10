from django.db import models

# Create your models here.
class Course(models.Model):
    cid=models.IntegerField(primary_key=True)
    cname=models.CharField(max_length=30)
    fees=models.FloatField()


    def __str__(self):
        return f'{self.cid}--{self.cname}--{self.fees}'

class Student(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    sid=models.IntegerField(unique=True)
    sname=models.CharField(max_length=30)
    dob=models.DateField()
    add=models.CharField(max_length=100)
    contact=models.BigIntegerField()
