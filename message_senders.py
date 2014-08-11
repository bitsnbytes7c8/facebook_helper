#Gets 50 threads (as that's the limit returned by FQL) given the starting and ending index

import urllib
import facebook
import json
import access_token
import fql
import userDetails;
import sys;

#Gets threads from start to end by using fql query
def get_fifty(start, end):
  token = access_token.get_token();
  query= "SELECT thread_id,updated_time FROM thread WHERE viewer_id=me() AND folder_id=0 LIMIT " + str(start) + "," + str(end);
  
  mesg_ids = fql.get_json(query, token);
  sender_names = {};
  if len(mesg_ids['data']) == 0:
    return None;
  try:
    for id in mesg_ids['data']:
      thread_id = id['thread_id'];
      time = id['updated_time'];
      query = "SELECT author_id from message WHERE thread_id="+thread_id;
      sent_ids = fql.get_json(query, token);
      try:
        for sent_id in sent_ids['data']:
          sender_id = sent_id['author_id']
          if sender_id is not '1310093194' and sender_id != 1310093194:
            name = userDetails.get_name_from_id(sender_id, token);
            if name not in sender_names.keys():
              sender_names[name] = sender_id;
            break;
      except KeyError:
        print sent_id['error']['message'];
        return None

  except TypeError as e:
    print e;
    return None;
  except KeyError as e:
    print mesg_ids['error']['message'];
    return None;
  return sender_names;
#friends = graph.get_connections("me", "friends")
#friends_list = [friend['id'] for friend in friends['data']]
#friends_name = [friend['name'] for friend in friends['data']]

#for id,name in zip(friends_list, friends_name): 
  #break;
  #print id + " " + name;
