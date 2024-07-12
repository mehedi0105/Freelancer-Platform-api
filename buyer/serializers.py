from rest_framework import serializers
from . import models

class JobSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.ADD_JOB
        fields = '__all__'

class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Reveiw
        fields = '__all__'

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'