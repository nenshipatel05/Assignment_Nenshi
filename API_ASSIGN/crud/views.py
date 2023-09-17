from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import (mixins, generics, status, permissions)
# Create your views here.
from .models import Blog
from .serializers import BlogSerializer
from rest_framework import viewsets


class  BlogModelViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class=BlogSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data['name']
            try:
                val = Blog.objects.get(name = data)
            except Blog.DoesNotExist:
                val = None
            if val is not None:
                return Response({'details : Blog with this name already exists'}, status=status.HTTP_400_BAD_REQUEST)
            else :  
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

