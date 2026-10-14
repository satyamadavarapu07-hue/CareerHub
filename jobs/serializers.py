from django.contrib.auth.models import User

from rest_framework import serializers
 

from .models import (
    Job,
    Application
)


class JobSerializer(serializers.ModelSerializer):

    class Meta:
        model = Job
        fields = "__all__"


class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only=True
    )

    class Meta:
        model = User

        fields = [
            "username",
            "email",
            "password",
        ]

    def create(self, validated_data):

        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
        )

        return user




class ApplicationSerializer(
    serializers.ModelSerializer
):

    class Meta:
        model = Application

        fields = [
            "id",
            "job",
            "resume",
            "status",
            "applied_at",
        ]

        read_only_fields = [
            "id",
            "status",
            "applied_at",
        ]