facebook_helper
===============

Contains python codes for programs using facebook api.
All the programs require that the facebook-sdk be present in the current working directory

# Running 
'python get_message_senders.py' 
will write to a function to get the names of all people who've sent messages to you to a file named 'outfile'. 
Required: Access token in a file named 'token.txt'.

# fql.py contains a function to call a fql query and return the data as a json object. It takes as input the query string and the access token.

# userDetails.py is a (half-written) program which contains functions to return the details about a user given the user id.

