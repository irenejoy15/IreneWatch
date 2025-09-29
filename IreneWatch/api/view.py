from rest_framework.response import Response
from watchlist_app.models import Movie
from IreneWatch.api.serializers import MovieSerializer
from rest_framework.decorators import api_view

@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    serialized_data = MovieSerializer(movies, many=True)
    return Response(serialized_data.data)

@api_view(['GET'])
def movie_detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    serialized_data = MovieSerializer(movie)
    return Response(serialized_data.data)