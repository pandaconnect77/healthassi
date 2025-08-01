
from django.db import models

class UserProfile(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    blood_group = models.CharField(max_length=5)
    height = models.FloatField()
    weight = models.FloatField()

    def __str__(self):
        return self.username


class HealthRecord(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True,related_name='health_records')
    message = models.TextField()
    bot_response = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.message

class SkinDisease(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='skin_diseases')
    image = models.ImageField(upload_to='skin_diseases/')
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.message[:30]