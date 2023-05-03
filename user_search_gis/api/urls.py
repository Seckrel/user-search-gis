from django.urls import path
from .viewset import (ListUserProfiles, PatchUserProfile)



app_name = "api"

urlpatterns = [
    path('list-users', ListUserProfiles.as_view(), name="list_users"),
    # path('add-user', ),
    path('update-user', PatchUserProfile.as_view(), name="updateuser"),
    # path('delete-user', ),
    
]
