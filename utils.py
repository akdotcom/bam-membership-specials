import urllib
import string
import random
try: import simplejson as json
except ImportError: import json

import foursquare

from config import CONFIG


def getServer():
  if CONFIG['local_dev']:
    return CONFIG['local_server']
  else:
    return CONFIG['prod_server']

def generateContentUrl(content_id):
  return CONFIG['content_uri'] % (getServer(), content_id)


def generateRedirectUri():
  return CONFIG['redirect_uri'] % getServer()


def generateFoursquareAuthUri(client_id):
  redirect_uri = generateRedirectUri()
  server = CONFIG['foursquare_server']
  url = '%s/oauth2/authenticate?client_id=%s&response_type=code&redirect_uri=%s'
  return url % (server, client_id, urllib.quote(redirect_uri))


def makeFoursquareClient(access_token=None):
  redirect_uri = generateRedirectUri()
  return foursquare.Foursquare(client_id = CONFIG['client_id'],
                               client_secret = CONFIG['client_secret'],
                               access_token = access_token,
                               redirect_uri = redirect_uri,
                               version = CONFIG['api_version'])


def generateId(size=20, chars=string.ascii_uppercase + string.digits):
  return ''.join(random.choice(chars) for _ in range(size))


def fetchJson(url):
  """Does a GET to the specified URL and returns a dict representing its reply."""
#  logging.info('fetching url: ' + url)
  result = urllib.urlopen(url).read()
#  logging.info('got back: ' + result)
  return json.loads(result)
