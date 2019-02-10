from rest_framework import  serializers
from .models import Stocks


class stocksSerializer(serializers.ModelSerializer):
    class Meta:
        model=Stocks
        #filter('firstName','lastName')
        fields = '__all__'