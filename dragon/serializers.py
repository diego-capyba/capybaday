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


class BattlePairSerializer(serializers.Serializer):
    dragon = serializers.PrimaryKeyRelatedField(queryset=Dragon.objects.all())
    rider = serializers.PrimaryKeyRelatedField(queryset=Rider.objects.all())


class DragonBattleSerializer(serializers.Serializer):
    left = BattlePairSerializer()
    right = BattlePairSerializer()

    def battle(self):
        left = self.validated_data['left']
        right = self.validated_data['right']

        left_power = left['dragon'].power + left['rider'].power
        right_power = right['dragon'].power + right['rider'].power

        if left_power > right_power:
            winner = "left"
        elif left_power == right_power:
            winner = None
        else:
            winner = "right"

        return winner
