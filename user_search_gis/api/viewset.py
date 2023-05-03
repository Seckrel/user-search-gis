from rest_framework.generics import ListAPIView, UpdateAPIView
from .serializer import UserProfileSerializer
from user.models import UserProfile


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
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        print(partial, request.data)
        instance = self.get_object()
        print(partial, instance)
        # serializer = self.get_serializer(instance, data=request.data, partial=partial)
        # serializer.is_valid(raise_exception=True)
        # self.perform_update(serializer)

        # if getattr(instance, '_prefetched_objects_cache', None):
        #     # If 'prefetch_related' has been applied to a queryset, we need to
        #     # forcibly invalidate the prefetch cache on the instance.
        #     instance._prefetched_objects_cache = {}

        # return Response(serializer.data)
    