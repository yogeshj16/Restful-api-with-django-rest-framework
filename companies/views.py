from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Stocks
from .serializers import stocksSerializer



class StocksList(APIView):
    def get(self, request):
        stock1=Stocks.objects.all()
        serializer = stocksSerializer(stock1, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializerList = stocksSerializer(Stocks ,data=request.data)
        if serializerList.is_valid():
            serializerList.save()
            return Response(serializerList.data, status=status.HTTP_201_CREATED)
        return Response(serializerList.error_messages, status=status.HTTP_400_BAD_REQUEST)

