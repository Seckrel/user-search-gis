from rest_framework.generics import (
    ListAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView)
from .serializer import UserProfileSerializer, UserSerializer, UserHomeOfficeGapSerializer
from user.models import UserProfile
from hometoofficelinevector.models import UserHomeOfficeGap
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import Response
from django.contrib.gis.measure import D
from django.contrib.gis.geos import Point
from math import pi


class ListUserProfiles(ListAPIView):
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        """
        Returns the queryset of UserProfile instances to be displayed.

        Returns:
            QuerySet: The queryset of UserProfile instances to be displayed.
        """

        queryset = UserProfile.objects.all()
        return queryset


class PatchUserProfile(UpdateAPIView):
    # TODO make area of interest updatable
    http_method_names = ['patch']
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]
    queryset = UserProfile.objects.all()
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        user = instance.user
        user.first_name = serializer.validated_data.get(
            'first_name', user.first_name)
        user.last_name = serializer.validated_data.get(
            'last_name', user.last_name)
        user.save()

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)


class RetriveUserProfile(RetrieveAPIView):
    http_method_names = ['get']
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'
    queryset = UserProfile.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class DeleteUser(DestroyAPIView):
    http_method_names = ['delete']
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'
    queryset = User.objects.all()

    def destory(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destory(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class RetriveUserHomeToOfficeLineVec(RetrieveAPIView):
    http_method_names = ['get']
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'
    serializer_class = UserHomeOfficeGapSerializer
    queryset = UserProfile.objects.all()

    def retrieve(self, request, *args, **kwargs):
        user_profile_id = self.kwargs.get('id')
        home_to_office_qs = UserHomeOfficeGap.objects.filter(
            user__id=user_profile_id)[0]
        print(home_to_office_qs)

        geo_json_data = self.get_serializer(home_to_office_qs)

        return Response(geo_json_data.data)


class ListHomeAddressInRange(ListAPIView):
    # TODO convert km to degree
    serializer_class = UserProfileSerializer
    
    def get_queryset(self):
        users = UserProfile.objects.all()
        return users

    def filter_queryset(self, queryset):
        search_radius_km: int = 10
        lat, log = self.request.data.values()
        ref_point = Point(lat, log)
        
        # km_to_degree = lambda radius_km: D(km=radius_km) / D(6371) * D(180) / D(pi) # given radius in km divded by earths mean radius which is 63471km then D(180) / D(pi) convert to degree

        try:
            qs = queryset.filter(home_address__dwithin=(
                ref_point, D(km=search_radius_km).m))
        except Exception as e:
            print(e)
            
        return qs
