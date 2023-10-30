from rest_framework import serializers
from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'slug', 'thumbnail',
                  'title', 'views', 'upload_datetime')
