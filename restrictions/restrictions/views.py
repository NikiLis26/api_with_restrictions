
from permissions import permissions
from models import Advertisement
from .serializers import AdvertisementSerializer
from django_filters.rest_framework import DateFromToRangeFilter
from rest_framework import filters, viewsets
from .permissions import IsAuthorOrReadOnly

class AdvertisementViewSet(viewsets.ModelViewSet):
   queryset = Advertisement.objects.all()
   serializer_class = AdvertisementSerializer
   filter_backends = (filters.OrderingFilter, filters.SearchFilter, DateFromToRangeFilter)
   search_fields = ['title', 'description']
   ordering_fields = ['created_at']
   permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

   def perform_create(self, serializer):
       serializer.save(author=self.request.user)
