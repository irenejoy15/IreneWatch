from asyncio import mixins
from rest_framework.response import Response
from watchlist_app.models import Watchlist,StreamPlatform,Review
from IreneWatch.api.serializers import ReviewSerializer, StreamPlatformSerializer, WatchlistSerializer
# from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins

class ReviewDetail(mixins.RetrieveModelMixin,generics.GenericAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

class ReviewList(mixins.ListModelMixin, mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class WatchListAV(APIView):
    def get(self, request):
        movies = Watchlist.objects.all()
        serialized_data = WatchlistSerializer(movies, many=True)
        return Response(serialized_data.data)
    
    def post(self, request):
        serialized_data = WatchlistSerializer(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data)
        else:
            return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
        
class WatchDetailAV(APIView):
    def get(self, request, pk):
        try:
            movie = Watchlist.objects.get(pk=pk)
            serialized_data = WatchlistSerializer(movie)
            return Response(serialized_data.data)
        except Watchlist.DoesNotExist:
            return Response({'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        movie = Watchlist.objects.get(pk=pk)
        serialized_data = WatchlistSerializer(movie, data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data)
        else:
            return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        movie = Watchlist.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT, data= {'message': 'Movie deleted successfully!'})
    
class StreamPlatformAV(APIView):
    def get(self, request):
        platforms = StreamPlatform.objects.all()
        serialized_data = StreamPlatformSerializer(platforms, many=True)
        return Response(serialized_data.data)
    
    def post(self, request):
        serialized_data = StreamPlatformSerializer(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data)
        else:
            return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
        
class StreamPlatformDetailAV(APIView):
    def get(self, request, pk):
        try:
            platform = StreamPlatform.objects.get(pk=pk)
            serialized_data = StreamPlatformSerializer(platform)
            return Response(serialized_data.data)
        except StreamPlatform.DoesNotExist:
            return Response({'error': 'Platform not found'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        platform = StreamPlatform.objects.get(pk=pk)
        serialized_data = StreamPlatformSerializer(platform, data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data)
        else:
            return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        platform = StreamPlatform.objects.get(pk=pk)
        platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT, data= {'message': 'Platform deleted successfully!'})