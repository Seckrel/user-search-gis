from rest_framework.generics import ListAPIView, UpdateAPIView, RetrieveAPIView
from .serializer import UserProfileSerializer
from user.models import UserProfile
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import Response



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
    http_method_names = ['patch']
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]
    queryset = UserProfile.objects.all()
    lookup_field = 'id'
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        
        user = instance.user
        user.first_name = serializer.validated_data.get('first_name', user.first_name)
        user.last_name = serializer.validated_data.get('last_name', user.last_name)
        user.save()

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)
    
class RetriveUserProfile(RetrieveAPIView):
    http_method_names = ['get']
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'
    