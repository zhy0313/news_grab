from rest_framework.serializers import  ModelSerializer
from .models import News, KeyWordList



class NewsSerializer(ModelSerializer):

    class Meta:

        model = News
        fields = ('news_source', 'title', 'url', 'pub_time')

class KeyWordSerializer(ModelSerializer):

    class Meta:

        model = KeyWordList
        fields = ('keyword', 'power')