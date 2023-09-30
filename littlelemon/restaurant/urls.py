from django.urls import path
from .views import BookingView,MenuView
from . import views
urlpatterns = [
    path('bookings/',BookingView.as_view(),name='bookings'),
    path('bookings/<id>',views.singleBookingView.as_view(),name='single'),

    path('menu/',MenuView.as_view(),name='bookings'),
    path('menu/<id>',views.singleMenuView.as_view(),name='single'),


   

]
