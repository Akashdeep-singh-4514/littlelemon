from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView,DestroyAPIView,RetrieveUpdateAPIView
#                                     (get post)            (delete put get)

from .models import Booking,Menu
from .serializers import BookingSerializer,MenuSerializer,UserSerializer,User
# from rest_framework.decorators import api_view

#                 get and post


from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class BookingView(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
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
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
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
    

class RegisterUser(APIView):
    def post(self,request):
        serializer=UserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'status':403,'errors':serializer.errors,'message':'something went wrong'})
        serializer.save()
        user=User.objects.get(username=serializer.data['username'])
        token_obj,_=Token.objects.get_or_create(user=user)
        return Response({'status':200,'payload':serializer.data,'token':str(token_obj),'message':'your data is saved'})