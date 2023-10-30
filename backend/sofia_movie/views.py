from django.shortcuts import render
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from .models import Movie
from .serializers import MovieSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class MovieListView(generics.ListAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pagination_class = PageNumberPagination
