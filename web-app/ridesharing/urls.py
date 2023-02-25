from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pendingRides/', views.PendingRideListView, name='PendingRideListView'),
    path('confirmedRides/', views.ConfirmedRideListView, name='ConfirmedRideListView'),
    path('confirmedRidesDriver/', views.ConfirmedRideDriverListView, name='ConfirmedRideDriverListView'),
    path('completedRidesDriver/', views.CompletedRideDriverListView, name='CompletedRideDriverListView'),
    path('joinRides/', views.JoinRideListView, name='JoinRideListView'),
    path('confirmedRide/<int:pk>', views.ConfirmRideView, name='ConfirmRideView'),
    path('joinRide/<int:ride_id>', views.JoinRideView, name='JoinRideView'),#add
    path('completedRide/<int:pk>', views.CompleteRideView, name='CompleteRideView'),#add
    path('driveropenRides/', views.DriverOpenRideListView, name='DriverOpenRideListView'),
    #path('shareropenRides/', views.SharerOpenRideListView, name='SharerOpenRideListView'),
    path('registerDriver/', views.RegisterDriverView, name='RegisterDriverView'),
    path('requestRide/', views.RequestRideView, name='RequestRideView'),
    path('registerUser/', views.RegisterUserView, name='RegisterUserView'),
    path('rides/', views.RideListView.as_view(), name='rides'),
    path('ride/<int:pk>', views.RideDetailView.as_view(), name='ride-detail'),
    path('editRide/<int:ride_id>', views.EditRideView, name='editRide'),
    #path('editProf/<int:pk>', views.EditProfView, name='editProf'),
    path('editProf/', views.EditProfView, name='editProf'), 
    #path(r'editProf/$', views.EditProfView, name='editProf'),
    path('editDriver/',views.EditDriverView, name='editDriverView'),
    path('searchRides/', views.SearchRideView, name='SearchRideView'),
    #new add
    path('sharesearchRides/', views.ShareSearchRideView, name='ShareSearchRideView'),
]

