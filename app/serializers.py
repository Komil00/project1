from abc import ABC

from rest_framework import serializers

from .models import Client, Device, Loan
from core.models import CustomUser


class DeviceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'


class ClientSerializers(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(queryset=CustomUser.objects.all(), slug_field='username')

    class Meta:
        model = Client
        fields = '__all__'


class LoanSerializer(serializers.Serializer):
    device = serializers.SlugRelatedField(queryset=Device.objects.all(), slug_field='model')
    client = serializers.SlugRelatedField(queryset=Client.objects.all(), slug_field='fullname')
    created = serializers.DateTimeField()
    updated = serializers.DateTimeField()
    payed = serializers.FloatField()
    first_pay = serializers.FloatField()
    end_date = serializers.DateTimeField()
    month_pay = serializers.FloatField()

    def create(self, validated_data):
        loan = Loan(
            device=validated_data['device'],
            client=validated_data['client'],
            created=validated_data['created'],
            updated=validated_data['updated'],
            payed=validated_data['payed'],
            first_pay=validated_data['first_pay'],
            end_date=validated_data['end_date'],
            month_pay=validated_data['month_pay'],
        )
        loan.save()
        return loan

