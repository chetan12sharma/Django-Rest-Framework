from rest_framework import serializers
from models import Competition, Drone, DroneCategory, Pilot
# from .views import


class DroneCategorySerializer(serializers.HyperlinkedModelSerializer):
    verbose_drone = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name='drone_details')

    class Meta:
        model = DroneCategory
        fields = ('url', 'pk', 'name', 'verbose_drone')


class DroneSerializer(serializers.HyperlinkedModelSerializer):
    drone_category = serializers.SlugRelatedField(
        queryset=DroneCategory.objects.all(), slug_field='name')

    class Meta:
        model = Drone
        fields = (
            'url',
            'name',
            'drone_category',
            'manufacturing_date',
            'has_it_competed', 'inserted_timestamp',)


class CompetitionSerailizer(serializers.HyperlinkedModelSerializer):
    drone = DroneSerializer()

    class Meta:
        model = Competition
        fields = (
            'url',
            'pk',
            'distance_in_feet',
            'distance_achievement_date',
            'drone',)


class PilotSerializer(serializers.HyperlinkedModelSerializer):
    competitions = serializers.HyperlinkedModelSerializer(
        many=True, read_only=True)
    gender = serializers.ChoiceField(choices=Pilot.choices)
    gender_description = serializers.CharField(
        source='get_gender_display', read_only=True)

    class Meta:
        model = Pilot
        fields = (
            'url',
            'name',
            'gender',
            'gender_description',
            'races_count',
            'inserted_timestamp',
            'competitions'
        )


class PilotCompetitionSerializer(serializers.ModelSerializer):
    pilot = serializers.SlugRelatedField(
        queryset=Pilot.objects.all(), slug_field='name')
    drone = serializers.SlugRelatedField(
        queryset=Drone.objects.all(), slug_field='name')

    class Meta:
        model = Competition
        fields = (
            'url',
            'pk',
            'pilot',
            'drone',
            'distance_in_feet',
            'distance_achivement_date',
        )
