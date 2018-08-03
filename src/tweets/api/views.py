from rest_framework import generics
from .serializers import TweetModelSerializer
from tweets.models import Tweet

class TweetListAPIView(generics.ListAPIView):
    serializer_class = TweetModelSerializer

    def get_queryset(self):
        return Tweet.objects.all()
    