from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class UserLoginActivity(models.Model):
    # Login Status
    SUCCESS = 'S'
    FAILED = 'F'

    LOGIN_STATUS = ((SUCCESS, 'Success'),
                           (FAILED, 'Failed'))

    login_IP = models.GenericIPAddressField(null=True, blank=True)
    login_datetime = models.DateTimeField(auto_now=True)
    login_username = models.CharField(max_length=40, null=True, blank=True)
    status = models.CharField(max_length=1, default=SUCCESS, choices=LOGIN_STATUS, null=True, blank=True)
    user_agent_info = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'user Activity'
        verbose_name_plural = 'user Activities'

    def __str__(self):
        return str(self.login_username)

class ConnectionUserProfile(models.Model):

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    title = models.CharField(max_length=5)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    dob = models.DateField()
    address = models.CharField(max_length=255)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zip = models.CharField(max_length=10)
    photo = models.ImageField(upload_to='uploads', blank=True)
    phone_number = PhoneNumberField(blank=True,null=True)
    fax_number = PhoneNumberField(blank=True,null=True)

    class Meta:
        verbose_name = 'connection User Profile'
        verbose_name_plural = 'connection User Profiles'

class Connections(models.Model):
    user_id = models.IntegerField(null=True, blank=True)
    connection_id =models.IntegerField(null=True, blank=True)
    created_at =  models.DateTimeField(auto_now_add=True,blank=True, null=True)
    updated_at =  models.DateTimeField(auto_now=True,blank=True, null=True)

    class Meta:
        verbose_name = 'connection'
        verbose_name_plural = 'connections'

    def __str__(self):
        return str(self.user_id)
