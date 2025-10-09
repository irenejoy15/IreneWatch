
from django.urls import path, include
# from IreneWatch.api.view import movie_list ,movie_detail
from IreneWatch.api.view import ReviewList, WatchDetailAV, WatchListAV, StreamPlatformAV, StreamPlatformDetailAV, ReviewDetail
urlpatterns = [
    path('list/', WatchListAV.as_view(), name='watchlist'),
    path('<int:pk>', WatchDetailAV.as_view(), name='watch-detail'),
    path('stream/list/', StreamPlatformAV.as_view(), name='stream-platform'),
    path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name='streamplatform-detail'),
    path('review', ReviewList.as_view(), name='review-list'),
    path('review/<int:pk>', ReviewDetail.as_view(), name='review-detail'),

]
