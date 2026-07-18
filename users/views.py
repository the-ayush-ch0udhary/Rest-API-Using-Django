from rest_framework import generics
from .models import UserProfile
from .serializers import UserProfileSerializer
from .permissions import IsOwner
from .filters import UserProfileFilter


class UserListCreateView(generics.ListCreateAPIView):
    serializer_class = UserProfileSerializer

    filterset_class = UserProfileFilter
    search_fields = ["user__username", "bio"]
    ordering_fields = ["id"]

    def get_queryset(self):
        return UserProfile.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [IsOwner]

    def get_queryset(self):
        return UserProfile.objects.filter(user=self.request.user)