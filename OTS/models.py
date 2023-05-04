from django.db import models

# Create your models here.

# Candidate Table
class Candidate(models.Model):
    username=models.CharField(primary_key=True,max_length=20)
    password=models.CharField(max_length=15,null=False)
    name=models.CharField(null=False,max_length=100)
    test_attempted=models.IntegerField()
    points=models.FloatField()

# Question Table
class Question(models.Model):
    qid=models.BigAutoField(primary_key=True,auto_created=True)
    ques=models.TextField()
    a=models.CharField(max_length=255)
    b=models.CharField(max_length=255)
    c=models.CharField(max_length=255)
    d=models.CharField(max_length=255)
    ans=models.CharField(max_length=255)

# Result Table

class Result(models.Model):
    resultid=models.BigAutoField(primary_key=True,auto_created=True)
    username=models.ForeignKey(Candidate,on_delete=models.CASCADE)
    date=models.DateField(auto_now=True)
    time=models.TimeField(auto_now=True)
    quest_attempt=models.IntegerField()
    right=models.IntegerField()
    wrong=models.IntegerField()
    points=models.FloatField()