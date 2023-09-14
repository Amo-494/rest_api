from django.shortcuts import render
from rest_framework import generics
from .models import Person
from .serializers import PersonSerializer


class PersonCreateView(generics.CreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonListView(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.query_params.get('name', None)  # Get the 'name' parameter from the request
        if name is not None:
            queryset = queryset.filter(name__icontains=name)  # Perform case-insensitive partial matching on the 'name' field
        return queryset
    
    
class PersonRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

