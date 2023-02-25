'''

'''
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings
from django.urls import reverse
import uuid
class Vehicle(models.Model):
    SEDAN = "SEDAN"
    MINIVAN = "MINI"
    CROSSOVER = "CROSS"
    CAR_CHOICES = (
        (SEDAN, 'Sedan'),
        (MINIVAN, 'Minivan'),
        (CROSSOVER, 'Crossover'),
    )
    #Type of the car
    type = models.CharField(
        max_length=10,
        choices= CAR_CHOICES,
        default=SEDAN,
        help_text='Vehicle type'
    )
    #License Plate Number
    plateNumber = models.CharField('plateNumber',
                                   max_length=8,
                                   help_text = "8 characters")
    FOUR = 4
    SIX = 6
    CAP_CHOICES = (
        (FOUR, 4),
        (SIX,6),
    )
    capacity = models.IntegerField(choices = CAP_CHOICES, default = FOUR)
    #vehicle_host = models.CharField(max_length=200,
    #                               default = "Please enter host name",
    #                               help_text="Enter a vehicle owner name", null = True)

    class Meta:
        verbose_name = 'Vehicle Info'

    def get_absolute_url(self):
        """Returns the url to access a particular book instance."""
        return reverse('vehicle-detail', args=[str(self.id)])
        
    def __str__(self):
        vehicle_info = self.type
        """String for representing the Model object (in Admin site etc.)"""
        return vehicle_info
    
class Prof(models.Model):
#    my_id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular book across whole library")
    isDriver = models.BooleanField(default=False)
    vehicle = models.OneToOneField(
        Vehicle,
        on_delete=models.SET_NULL,
        null = True,
        blank = True
    )    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    class Meta:
        verbose_name = 'User Profile'

    def get_absolute_url(self):
        """Returns the url to access a particular book instance."""
        return reverse('profile-detail', args=[str(self.id)])
        
    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.user.__str__()



@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Prof.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    post_save.disconnect(save_user_profile, sender=User)
    instance.profile.save()
    post_save.connect(save_user_profile, sender=User)


    
class Ride(models.Model):
    owner = models.ForeignKey(Prof, on_delete=models.CASCADE, related_name="owner_set")
    sharers = models.ManyToManyField(Prof, related_name="sharers_set")
    driver = models.ForeignKey(Prof, on_delete = models.CASCADE,null=True,blank=True,related_name = "driver_set")    
    pickUpTime = models.DateTimeField()
    isConfirmed = models.BooleanField(default=False)
    isComplete = models.BooleanField(default=False)
    canBeShared = models.BooleanField(default=False)
    SEDAN = "SEDAN"
    MINIVAN = "MINI"
    CROSSOVER = "CROSS"
    CAR_CHOICES = (
        (SEDAN, 'Sedan'),
        (MINIVAN, 'Minivan'),
        (CROSSOVER, 'Crossover'),
    )
    #Type of the car
    type = models.CharField(
        max_length=10,
        choices= CAR_CHOICES,
        default = "",
        blank = True,
        help_text='Vehicle type'
    )
    FOUR = 4
    SIX = 6
    CAP_CHOICES = (
        (FOUR, 4),
        (SIX,6),
    )
    capacity = models.IntegerField(choices = CAP_CHOICES, default = FOUR)
    destination = models.CharField(max_length=100,default="",help_text="Please enter a destination")
    total_passenger = models.IntegerField(default = 1)
    def display_sharers(self):
        return ', '.join([sharers.__str() for sharers in self.sharers.all()[:3]])

    display_sharers.short_description = 'Sharers'

    #add
    '''
    def sum_passengers(self):
        for sharer in ride.ride_party.all:
            total_passenger+=sharer.num_pass+1
        return total_passenger
    '''
    
    class Meta:
        ordering = ['pickUpTime']
        verbose_name = 'Ride Info'
        
    def count_sharers(self):
        return self.sharers.all().count()

    def display_sharers(self):
        """Creates a string for the Genre. This is required to display genre in Admin."""
        return ', '.join([sharers.__str__() for sharer in self.sharers.all()])

    display_sharers.short_description = 'Sharers'
    
    def get_absolute_url(self):
        """Returns the url to access a particular book instance."""
        return reverse('ride-detail', args=[str(self.id)])

        
    def __str__(self):
        rideinfo = 'Owner: '+self.owner.__str__()
        """String for representing the Model object (in Admin site etc.)"""
        return rideinfo


class Party(models.Model):
    ride = models.ForeignKey(Ride, on_delete=models.CASCADE, related_name="ride_party")
    sharer = models.ForeignKey(Prof, on_delete=models.CASCADE, related_name="sharer_party")
    num_pass = models.IntegerField(default = 1)
    '''
    def get_sum_pass(self):
        for share in ride.sharers:
            num_pass=num_pass+sharers
    '''
