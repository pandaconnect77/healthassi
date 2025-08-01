from rest_framework import serializers

from .models import UserProfile, HealthRecord, SkinDisease

class userProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'
        
class HealthRecordSerializer(serializers.ModelSerializer):
    user = userProfileSerializer(read_only=True)
    class Meta:
        model = HealthRecord
        fields = '__all__'

class SkinDiseaseSerializer(serializers.ModelSerializer):
    user = userProfileSerializer(read_only=True)
    class Meta:
        model = SkinDisease
        fields = '__all__'