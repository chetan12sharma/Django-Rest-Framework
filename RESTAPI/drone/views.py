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
# * For authentication and permission
from rest_framework import permissions
# * For basic authentication and session authentication
from .custompermission import IsCurrentUserOwnerOrReadOnly

# !For filtering seaching and ordering
from django_filters import AllValuesFilter, NumberFilter, DateTimeFilter
from django_filters import FilterSet


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
        'race_count',
    )
    search_fields = (
        '^name',
    )
    ordering_fields = (
        'name',
        'race_count'
    )


# !for Chetan
# <Token: 27f358b52bad66bc209758a61df8ce45cbeed315>

# !For Neeraj
# <Token: e71aafd7177712f6855b6374a8504d9e7affa47c >


class PilotDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pilot.objects.all()
    serializer_class = PilotSerializer
    name = 'pilot-detail'


class CompetitionList(generics.ListCreateAPIView):
    queryset = Competition.objects.all()
    serializer_class = PilotCompetitionSerializer
    name = 'competition-list'
    filter_fields = (
        'distance_in_feet',
        'distance_achivement_date',
        'drone',
        'pilot',
    )
    search_fields = (
        '^name',
    )
    ordering_fields = (
        'name',
    )


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

    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsCurrentUserOwnerOrReadOnly
    )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class DroneDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer
    name = "drone-detail"

    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsCurrentUserOwnerOrReadOnly
    )
