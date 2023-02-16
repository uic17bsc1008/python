from django.db import models

class Course(models.Model):
    coursename = models.CharField(max_length=200)
    duration = models.CharField(max_length=200)
    fees = models.FloatField()
    course_code = models.CharField(max_length=4, null=True)
    remark = models.TextField()

    def __str__(self):
        return self.coursename

class Batch(models.Model):
    name = models.CharField(max_length=200)
    batch_co_ordinator = models.CharField(max_length=200)
    timming = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Centre(models.Model):
    name = models.CharField(max_length=200)
    center_owner = models.CharField(max_length=100, null=True)
    phone = models.IntegerField()
    email = models.EmailField(max_length=100, null=True)
    location = models.TextField()
    centre_category = models.CharField(max_length=50, null=True)
    centre_code = models.CharField(max_length=4, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Student(models.Model):
    enroll = models.CharField(max_length=200, null=True) 
    fullname = models.CharField(max_length=200)
    phone = models.IntegerField()
    email = models.EmailField(max_length=200)
    address = models.TextField()
    guardian = models.CharField(max_length=200)
    reference = models.CharField(max_length=200)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    batch = models.ForeignKey(Batch, on_delete=models.SET_NULL, null=True)
    centre = models.ForeignKey(Centre, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.fullname