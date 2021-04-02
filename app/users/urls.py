from django.urls import include, path
from rest_framework import routers

from .views import UsersViewSet, UserProfileViewSet, InstructorProfileViewSet, UserProfileByStudyGroup

router = routers.DefaultRouter()
router.register("users", UsersViewSet, basename="user")
router.register("profiles", UserProfileViewSet, basename="user-profile")
router.register("instructors", InstructorProfileViewSet, basename="instructor-profile")

urlpatterns = [
    path('', include(router.urls)),
    path('users/group/<str:group>/', UserProfileByStudyGroup.as_view(), name="user-group-list"),
]