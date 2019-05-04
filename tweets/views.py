from django.conf import settings
from django.shortcuts import render

from twython import Twython


def index(request):
    twitter = Twython(settings.TWITTER_API_KEY, access_token=settings.TWITTER_ACCESS_TOKEN)
    response = twitter.search(q='#mlhlocalhost')
    tweets = response['statuses']
    context = {
        'tweets': tweets
    }
    return render(request, 'tweets/index.html', context)
    