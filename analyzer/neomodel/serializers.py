from rest_framework import serializers


class GroupSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    objectSid = serializers.CharField()
    distinguishedName = serializers.CharField()
    description = serializers.CharField()
    whenCreated = serializers.DateField()
    securityDescriptor = serializers.CharField()
    genericAll = serializers.BooleanField()
    writeDacl = serializers.BooleanField()


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    objectSid = serializers.CharField()
    distinguishedName = serializers.CharField()
    servicePrincipalName = serializers.CharField()
    securityDescriptor = serializers.CharField()
    whenCreated = serializers.DateField()
    pwdLastSet = serializers.DateField()
    genericAll = serializers.BooleanField()
    writeDacl = serializers.BooleanField()


class ComputerSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    objectSid = serializers.CharField()
    distinguishedName = serializers.CharField()
    operatingSystem = serializers.CharField()
    securityDescriptor = serializers.CharField()
    whenCreated = serializers.DateField()
