from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import employees
from .serializers import emloyeeSerializer


class employeesList(APIView):

    def get(self, request):
        employeel1=employees.objects.all()
        serializer=emloyeeSerializer(employeel1,many=True)
        return Response(serializer.data)
    def post(self):
        pass
