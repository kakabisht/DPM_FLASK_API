from django.shortcuts import render
from rest_framework import generics
from .serializers import BucketlistSerializer
from .models import Bucketlist


class CreateView(generics.ListCreateAPIView):
    # The ListCreateAPIView is a generic view which provides GET (list all) and POST method handlers
    """This class defines the create behavior of our rest api."""
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    # RetrieveUpdateDestroyAPIView is a generic view that provides GET(one), PUT, PATCH and DELETE method handlers.
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer