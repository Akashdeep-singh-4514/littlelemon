from django.urls import path
from . import views
urlpatterns = [
    path('bookings/',views.BookingView.as_view(),name='bookings'),
    path('bookings/<id>/',views.singleBookingView.as_view(),name='single'),

    path('menu/',views.MenuView.as_view(),name='bookings'),
    path('menu/<id>/',views.singleMenuView.as_view(),name='single'),

    path('register/',views.RegisterUser.as_view(),name='register')
   

]
