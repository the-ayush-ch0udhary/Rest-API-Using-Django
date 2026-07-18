import django_filters

from .models import UserProfile

class UserProfileFilter(django_filters.FilterSet):
    created_at = django_filters.DateFilter(field_name = "created_at")

    class Meta:
        model = UserProfile
        fields = ["created_at"]