from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView,DestroyAPIView,RetrieveUpdateAPIView
#                                     (get post)            (delete put get)

from .models import Booking,Menu
from .serializers import BookingSerializer,MenuSerializer
# from rest_framework.decorators import api_view

#                 get and post
class BookingView(APIView):
    def get(self,request):
        items=Booking.objects.all()
        serializer=BookingSerializer(items,many=True)
        return Response(serializer.data) #return JSON
    def post(self,request):
        serializer=BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response({'status':'success','data':serializer.data})
    
class singleBookingView(APIView):
    def get(self,request,id):
        try:
            item=Booking.objects.get(id=id)
        except Booking.DoesNotExist:
            msg={'msg':'not found'}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)
        serializer=BookingSerializer(item)
        return Response(serializer.data,status=status.HTTP_200_OK)
       
    def put(self,request,id):
        try:
            item=Booking.objects.get(id=id)
        except Booking.DoesNotExist:
            msg={'msg':'not found'}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)
        
        serializer=BookingSerializer(item,data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response({'status':'success','data':serializer.data})
    def delete(self,request,id):
        try:
            item=Booking.objects.get(id=id)
        except Booking.DoesNotExist:
            msg={'msg':'not found'}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)
        item.delete()
        return Response({'status':'success'})
    



class MenuView(APIView):
    def get(self,request):
        items=Menu.objects.all()
        serializer=MenuSerializer(items,many=True)
        return Response(serializer.data) #return JSON
    def post(self,request):
        serializer=MenuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response({'status':'success','data':serializer.data})
    
class singleMenuView(APIView):
    def get(self,request,id):
        try:
            item=Menu.objects.get(id=id)
        except Menu.DoesNotExist:
            msg={'msg':'not found'}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)
        serializer=MenuSerializer(item)
        return Response(serializer.data,status=status.HTTP_200_OK)
       
    def put(self,request,id):
        try:
            item=Menu.objects.get(id=id)
        except Menu.DoesNotExist:
            msg={'msg':'not found'}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)
        
        serializer=MenuSerializer(item,data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response({'status':'success','data':serializer.data})
    def delete(self,request,id):
        try:
            item=Menu.objects.get(id=id)
        except Menu.DoesNotExist:
            msg={'msg':'not found'}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)
        item.delete()
        return Response({'status':'success'})
    

