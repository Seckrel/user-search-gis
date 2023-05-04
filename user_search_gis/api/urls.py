from django.urls import path
from .viewset import (ListUserProfiles, PatchUserProfile,
                      RetriveUserProfile, DeleteUser, RetriveUserHomeToOfficeLineVec, ListHomeAddressInRange)


app_name = "api"

urlpatterns = [
    path('list-users', ListUserProfiles.as_view(), name="list_users"),
    path('update-user/<int:id>', PatchUserProfile.as_view(), name="updateuser"),
    path('retrive-user/<int:id>', RetriveUserProfile.as_view(), name="retriveuser"),
    path('delete-user/<int:id>', DeleteUser.as_view(), name="deleteuser"),
    path('home-to-office/<int:id>', RetriveUserHomeToOfficeLineVec.as_view(),
         name="userhometoofficelinevec"),
    path('search-home', ListHomeAddressInRange.as_view(), name="searchhome")
]
