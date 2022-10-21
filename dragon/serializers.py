from rest_framework import serializers

from .models import Dragon, Location, Rider


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = [
            'id',
            'name',
        ]


class RiderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rider
        fields = [
            'id',
            'name',
        ]


class DragonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dragon
        fields = [
            'id',
            'name',
            'color',
            'weight',
            'location',
            'riders',
        ]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['location'] = LocationSerializer(instance=instance.location).data
        data['riders'] = RiderSerializer(instance=instance.riders, many=True).data
        return data
