from django.shortcuts import render

from books.models import Book
from rest_framework.decorators import api_view
from books.serializers import bookserializer,userserializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated,AllowAny



# @api_view(['GET','POST'])
# def booklist(request):#non primary key
#     if(request.method=="GET"):
#         books=Book.objects.all()
#         s=bookserializer(books,many=True)
#         return Response(s.data)
#     elif(request.method=="POST"):
#         s=bookserializer(data=request.data)
#         if s.is_valid():
#             s.save()
#             return Response(s.data,status=status.HTTP_201_CREATED)
#     return Response(s.errors,status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET','PUT','DELETE'])
# def book_details(request,pk):#primary based key
#     try:
#         books=Book.objects.get(pk=pk)
#     except:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if(request.method=="GET"):
#         s=bookserializer(books)
#         return Response(s.data)
#     elif(request.method=="PUT"):
#         s = bookserializer(books,data=request.data)
#         if s.is_valid():
#             s.save()
#             return Response(s.data, status=status.HTTP_201_CREATED)
#         return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif(request.method=="DELETE"):
#             books.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)






from rest_framework import mixins,generics,viewsets




# class booklist(generics.ListCreateAPIView):#non primary keu
#     queryset=Book.objects.all()
#     serializer_class=bookserializer
#
# class bookdetail(generics.RetrieveUpdateDestroyAPIView):#primary key based
#     queryset = Book.objects.all()
#     serializer_class = bookserializer



class bookviewset(viewsets.ModelViewSet):#primary key based and non primary key based\
    permission_classes = [IsAuthenticated,]
    queryset = Book.objects.all()
    serializer_class=bookserializer

class userviewset(viewsets.ModelViewSet):#primary key based and non primary key based
    # permission_classes = [AllowAny,]
    queryset = User.objects.all()
    serializer_class=userserializer

# class usercreate(generics.ListCreateAPIView):#it doesn't have PUT and DELETE
#     queryset = User.objects.all()
#     serializer_class=userserializer
