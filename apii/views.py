from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse ,HttpResponseRedirect
from .models import *
# Create your views here.
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import serializers




class apiSerializer(serializers.ModelSerializer):
    class Meta:
        model= Apicheck
        fields='__all__'


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def show(request):
#    return HttpResponse("hsishksjk")
    data = Apicheck.objects.all()
    context ={
           'data':data
          }
    serializerd= apiSerializer(data ,many=True)
    return Response(serializerd.data)


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def details(request,pk):
    # return HttpResponse("hsishksjk")
    data = Apicheck.objects.get(id=pk)
    serializerd= apiSerializer(data ,many=False)
    return Response(serializerd.data)

@api_view(['POST','GET',])
@permission_classes((permissions.AllowAny,))
def create(request):
#   return HttpResponse("hsishksjk")
    #data = request.data
    serializerd= apiSerializer(data=request.data)
    if serializerd.is_valid():
        serializerd.save()
    return Response(serializerd.data)

@api_view(['DELETE'])
@permission_classes((permissions.AllowAny,))
def delete(request,pk):
    # return HttpResponse("hsishksjk")
    data = Apicheck.objects.get(id=pk)
    data.delete()
    return HttpResponseRedirect(reverse('show'))


@api_view(['POST','GET'])
@permission_classes((permissions.AllowAny,))
def update(request,pk):
    # return HttpResponse("hsishksjk")
    datax = Apicheck.objects.get(id=pk)
    serializerd= apiSerializer(instance=datax,data=request.data)
    if serializerd.is_valid():
        serializerd.save()

    return Response(serializerd.data)
