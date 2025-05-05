from rest_framework import serializers
from .models import Parent, Child

class ChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        fields = ['id', 'first_name', 'last_name', 'birth_date', 'parent']

class ParentSerializer(serializers.ModelSerializer):
    children = ChildSerializer(many=True, read_only=True)
    
    class Meta:
        model = Parent
        fields = ['id', 'first_name', 'last_name', 'email', 'phone_number', 'children']
