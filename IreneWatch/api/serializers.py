from rest_framework import serializers
from watchlist_app.models import Watchlist,StreamPlatform

class WatchlistSerializer(serializers.ModelSerializer):
    len_title = serializers.SerializerMethodField()
    def get_len_title(self, object):
        return len(object.title)
    
    class Meta:
        model = Watchlist
        fields = '__all__'
        # fields = ['id', 'name', 'description', 'active']
        # exclude = ['active']

class StreamPlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = StreamPlatform
        fields = '__all__'
