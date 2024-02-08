from django.shortcuts import render
from rest_framework import viewsets, status
from products.models import Catagory, product, ForCart
from products.serializers import CategorySerializer, productSerializer, ProductDetailSerializer, addtocartSerializer,displaycartSerializer
from rest_framework.generics import ListAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.response import Response
import requests
from django.core.files.uploadedfile import File
import os

class categoryViewSet(viewsets.ModelViewSet):
    queryset = Catagory.objects.all()
    serializer_class = CategorySerializer

class productViewSet(viewsets.ModelViewSet):
    queryset = product.objects.all()
    serializer_class = productSerializer

class displaycartViewSet(viewsets.ModelViewSet):
    queryset = ForCart.objects.all()
    serializer_class = displaycartSerializer 

class addtocartViewSet(CreateModelMixin, GenericViewSet):
    queryset = ForCart.objects.all()
    serializer_class = addtocartSerializer 

    # def perform_create(self, serializer):
    #     if serializer.validated_data.get('image'):
    #         image_url = serializer.validated_data['image']
    #         image_response = requests.get(image_url)
    #         image_data = image_response.content

    #         # Create a new Django File object from the image data
    #         image = File(image_data, name=os.path.basename(image_url))

    #         # Save the image to the database
    #         serializer.validated_data['image'] = image

    #         # Save the object to the database
    #         serializer.save()

    #         return Response(serializer.data, status=status.HTTP_201_CREATED)

class ProductDetailViewSet(viewsets.ModelViewSet):
    queryset = product.objects.all()
    serializer_class = ProductDetailSerializer
    lookup_field = 'pk'
