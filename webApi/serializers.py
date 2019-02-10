from rest_framework import  serializers
from .models import employees


class emloyeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=employees
        #filter('firstName','lastName')
        fields = '__all__'