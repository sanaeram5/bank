import django_filters
from .models import *

class BranchFilter(django_filters.FilterSet):
    class Meta:
        model:Bank
        fields='__all__'
