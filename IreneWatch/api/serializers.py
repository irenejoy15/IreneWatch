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
    # HAS MANY ALL FIELDS OF WATCHLIST
    watchlist = WatchlistSerializer(many=True, read_only=True)
    # watchlist = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    # NASA VIEW.PY
    # watchlist = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='watch-detail')
    class Meta:
        model = StreamPlatform
        fields = '__all__'
