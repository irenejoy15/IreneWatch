from rest_framework.response import Response
from watchlist_app.models import Movie
from IreneWatch.api.serializers import MovieSerializer
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET','POST'])
def movie_list(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serialized_data = MovieSerializer(movies, many=True)
        return Response(serialized_data.data)
    
    if request.method == 'POST':
        serialized_data = MovieSerializer(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data)
        else:
            return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def movie_detail(request, pk):
    if request.method == 'GET':
        try:
            movie = Movie.objects.get(pk=pk)
            serialized_data = MovieSerializer(movie)
            return Response(serialized_data.data)
        except Movie.DoesNotExist:
            return Response({'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        movie = Movie.objects.get(pk=pk)
        serialized_data = MovieSerializer(movie, data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data)
        else:
            return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
        
    if request.method == 'DELETE':
        movie = Movie.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT, data= {'message': 'Movie deleted successfully!'})