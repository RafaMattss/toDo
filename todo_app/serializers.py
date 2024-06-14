from rest_framework import serializers
from .models import Todo, Category, Profile

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'user', 'title', 'is_active', 'category', 'content', 'created_at', 'updated_at']
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'user', 'title', 'is_active', 'created_time']
        read_only_fields = ['id', 'user', 'created_time']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'user', 'is_active', 'description']
        read_only_fields = ['id', 'user']
