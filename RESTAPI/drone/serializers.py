from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Competition, Drone, DroneCategory, Pilot
from .views import *
from django.utils.translation import ugettext_lazy as _


class DroneCategorySerializer(serializers.HyperlinkedModelSerializer):
    drones = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name='drone-detail')

    class Meta:
        model = DroneCategory
        # fields = ("__all__")
        fields = ('url', 'pk', 'name', 'drones')


class DroneSerializer(serializers.HyperlinkedModelSerializer):
    drone_category = serializers.SlugRelatedField(
        queryset=DroneCategory.objects.all(), slug_field='name')
    # display the owner username
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Drone
        fields = (
            'url',
            'name',
            'owner',
            'drone_category',
            'manufacturing_date',
            'has_it_competed', 'inserted_timestamp',)


class CompetitionSerializer(serializers.HyperlinkedModelSerializer):
    drone = DroneSerializer()

    class Meta:
        model = Competition
        fields = (
            'url',
            'pk',
            'distance_in_feet',
            'distance_achivement_date',
            'drone',)


class PilotSerializer(serializers.HyperlinkedModelSerializer):
    competitions = CompetitionSerializer(
        many=True, read_only=True)
    gender = serializers.ChoiceField(choices=Pilot.GENDER_CHOICE)
    gender_description = serializers.CharField(
        source='get_gender_display', read_only=True)

    class Meta:
        model = Pilot
        fields = (
            'url',
            'name',
            'gender',
            'gender_description',
            'race_count',
            'inserted_timestamp',
            'competitions',
        )


class PilotCompetitionSerializer(serializers.ModelSerializer):
    pilot = serializers.SlugRelatedField(
        queryset=Pilot.objects.all(), slug_field='name')
    # drone = serializers.SlugRelatedField(
    #     queryset=Drone.objects.all(), slug_field='name')
    drone = Drone.objects.all()

    class Meta:
        model = Competition
        fields = (
            'url',
            'pk',
            'name',
            'pilot',
            'drone',
            'distance_in_feet',
            'distance_achivement_date',
        )


class UserDroneSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Drone
        fields = ('url', 'name')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    drones = UserDroneSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('url', 'pk', 'username', 'drone')
