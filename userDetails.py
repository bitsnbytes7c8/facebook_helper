#Returns user details given user id
# Requires to be present in the same directory as the facebook-sdk

import facebook
import json
import fql;

#Returns user's name given user id and access token
def get_name_from_id(uid, token):
  query = "SELECT name FROM user WHERE uid="+str(uid);
  name_json = fql.get_json(query, token);
  name = name_json['data'];
  for n in name:
    return n['name'];

#Returns users details given the detail required, user id and access_token
def get_detail_from_id(detail, uid, token):
  query = "SELECT" + detail + "FROM user WHERE uid="+str(uid);
  detail_json = fql.get_json(query, token);
  detail = detail_json['data'];
  for d in detail:
    return d[detail];
