from django.shortcuts import render
from .models import Drone, DroneCategory, Pilot, Competition
from .serializers import (
    DroneSerializer,
    PilotSerializer,
    PilotCompetitionSerializer,
    DroneCategorySerializer,
)
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.reverse import reverse

# For filtering seaching and ordering
from django_filters import AllValuesFilter, NumberFilter, DateTimeFilter
from rest_framework import filters


class ApiRoot(generics.GenericAPIView):
    name = "api-root"

    def get(sel, request, *args, **kwargs):
        return Response({
            "drone-categories": reverse(DroneCategoryList.name,
                                        request=request),
            "drone": reverse(DroneList.name, request=request),
            "competition": reverse(CompetitionList.name, request=request),
            "pilot": reverse(PilotList.name, request=request),
        })


class DroneCategoryList(generics.ListCreateAPIView):
    queryset = DroneCategory.objects.all()
    serializer_class = DroneCategorySerializer
    name = "dronecategory-list"

    # For filtering seaching and ordering
    filter_fields = (
        'name',
    )
    search_fields = (
        '^name',
    )
    ordering_fields = (
        'name',
    )


class DroneCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DroneCategory.objects.all()
    serializer_class = DroneCategorySerializer
    name = 'dronecategory-detail'


class PilotList(generics.ListCreateAPIView):
    queryset = Pilot.objects.all()
    serializer_class = PilotSerializer
    name = 'pilot-list'
    filter_fields = (
        'name',
        'gender',
        'races_count',
    )
    search_fields = (
        '^name',
    )
    ordering_fields = (
        'name',
        'races_count'
    )


class PilotDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pilot.objects.all()
    serializer_class = PilotSerializer
    name = 'pilot-detail'


class CompetitionList(generics.ListCreateAPIView):
    queryset = Competition.objects.all()
    serializer_class = PilotCompetitionSerializer
    name = 'competition-list'


class CompetitionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Competition.objects.all()
    serializer_class = PilotCompetitionSerializer
    name = "competition-detail"


class DroneList(generics.ListCreateAPIView):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer
    name = "drone-list"
    filter_fields = (
        'name',
        'drone_category',
        'manufacturing_date',
        'has_it_competed',
    )
    search_fields = (
        '^name',
    )
    ordering_fields = (
        'name',
        'manufacturing_date',
    )


class DroneDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer
    name = "drone-detail"
