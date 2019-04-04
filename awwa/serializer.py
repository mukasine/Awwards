from rest_framework import serializers
from .models import Project, Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('username', 'profile_image', ' bio', 'contact')

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('title', 'image', ' link', 'description', 'pub_date')

