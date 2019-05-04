# MLH Localhost Tweets
A demo application showing how to search and display tweets

## Installation
For this application, you will need:
- A [Twitter](https://twitter.com/) account with [developer access](#twitter)
- [Python](https://www.python.org/downloads) (3.5+)
- [Django](https://www.djangoproject.com/)
- [Twython](https://twython.readthedocs.io/)

1. Clone this repository.
2. Run `pip install -r requirements.txt` to install dependencies if you have not already.
3. Find your Twitter app credentials ([instructions](#twitter)).
4. Store the two keys as TWITTER_API_KEY and TWITTER_API_SECRET as environment variables. This can be through your [computer's environment variables](https://www.twilio.com/blog/2017/01/how-to-set-environment-variables.html), but we recommend using a virtual environment tool like [virtualenv](https://virtualenv.pypa.io/) or [conda](https://conda.io/).
5. Run `python manage.py runserver`.
6. Go to the URL, [127.0.0.1:8000](http://127.0.0.1:8000/), in a browser.

### <a name="twitter"></a> Twitter Developer Access
1. Apply for a developer account at [developer.twitter.com](https://developer.twitter.com/). Note, you'll need a Twitter account that's associated with a valid phone number before you can apply for a developer account. In the application, you'll have to explain what you plan to use your developer access for. When you do, you should use the example template that appears in that question's tooltip.
2. Wait for developer account access. This can take anywhere from a few hours to a few days. If you're planning on using Twitter APIs for a hackathon, you should apply at least a few days _before_ the hackathon starts.
3. Create an app in the Twitter dashboard at [developer.twitter.com/apps](https://developer.twitter.com/en/apps). Fill out the required fields. Note, for the "website" field, if you don't have a website, you can use your Github profile. If you don't have a Github profile, you can use any website profile you are associated with.
4. In the list of your apps at [developer.twitter.com/apps](https://developer.twitter.com/en/apps), click on Details > Keys and tokens. You should see two consumer API keys, an API key and a API secret key. These will come into play when we're making calls to the Twitter API.


