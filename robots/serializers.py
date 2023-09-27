from rest_framework import serializers
from robots.models import Robot


class RobotCreateSerializer(serializers.ModelSerializer):
    model = serializers.CharField(min_length=2, max_length=2)
    version = serializers.CharField(min_length=2, max_length=2)
    created = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Robot
        fields = ('model', 'version', 'created')
    
    def create(self, validated_data):
        serial = f"{validated_data['model']}-{validated_data['version']}"
        return Robot.objects.create(serial=serial, **validated_data)