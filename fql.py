# Calls fql query given the query and access token

import urllib
import json

#Given fql query and access_token returns the output string as a json
def get_json(query, access_token):
  params = urllib.urlencode({'q':query, 'access_token':access_token});
  url = "https://graph.facebook.com/fql?"+params;
  data = urllib.urlopen(url).read();
  rjson = json.loads(data);
  return rjson;

