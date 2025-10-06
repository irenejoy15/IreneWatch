
from django.urls import path, include
# from IreneWatch.api.view import movie_list ,movie_detail
from IreneWatch.api.view import MovieListAV, MovieDetailAV
urlpatterns = [
    path('list/', MovieListAV.as_view(), name='movie-list'),
    path('<int:pk>', MovieDetailAV.as_view(), name='movie-detail'),
]
