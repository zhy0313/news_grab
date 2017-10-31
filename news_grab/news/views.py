from .models import News, KeyWordList
from .serializers import NewsSerializer, KeyWordSerializer
from rest_framework import generics
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q

# Create your views here.

class NewsList(generics.ListAPIView):

    queryset = News.objects.all()
    serializer_class = NewsSerializer

class KeyWordList(generics.ListAPIView):

    queryset = KeyWordList.objects.all()
    serializer_class = KeyWordSerializer

class GetHotNews(APIView):

    def get(self, request, kw):

        KWNews = News.objects.filter(Q(title__contains=kw))
        serializer = NewsSerializer(KWNews, many=True)
        return Response(serializer.data)

def index(request):
    return render(request, "index.html")

def kw(request, kw):

    res = dict(kw=kw)
    return render(request, "keyword.html", res)