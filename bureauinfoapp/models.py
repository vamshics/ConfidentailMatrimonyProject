from django.db import models

#Create your models here.
class Age(models.Model):
    age = models.CharField(max_length=20)
    def __str__(self):
        return self.age
class Stateadd(models.Model):
    state1 = models.CharField(max_length=20)
    def __str__(self):
        return self.state1
class Create_Profile(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.EmailField()
    phoneno = models.IntegerField()
    gender = models.CharField(max_length=20)
    age = models.ForeignKey(Age, on_delete=models.CASCADE)
    hobbies = models.CharField(max_length=30)
    state = models.ForeignKey(Stateadd, on_delete=models.CASCADE)
    city = models.CharField(max_length=20)
    about = models.CharField(max_length=50)
    upload = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.firstname