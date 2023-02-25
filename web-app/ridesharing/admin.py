from django.contrib import admin

# Register your models here.
#from ridesharing.models import RideOwner, RideSharer, Driver, Vehicle, RideOrder
#from ridesharing.models import RideOwner, RideSharer, Driver, RideOrder
from ridesharing.models import Vehicle, Prof, Ride, Party

#admin.site.register(Vehicle)

#admin.site.register(Profile)

#admin.site.register(Ride)
#admin.site.register(Vehicle)
#admin.site.register(RideOrder)

# Define the admin class

class VehicleAdmin(admin.ModelAdmin):
    list_display = ('type', 'plateNumber', 'capacity')

# Register the admin class with the associated model
admin.site.register(Vehicle, VehicleAdmin)

class ProfAdmin(admin.ModelAdmin):
    list_display = ('user','isDriver', 'vehicle')
admin.site.register(Prof, ProfAdmin)

class RideAdmin(admin.ModelAdmin):
    list_display = ('owner', 'driver','pickUpTime','isConfirmed','isComplete','destination')
    #pass
admin.site.register(Ride, RideAdmin)

class PartyAdmin(admin.ModelAdmin):
    list_display = ('ride', 'sharer','num_pass')
    #pass
admin.site.register(Party, PartyAdmin)
