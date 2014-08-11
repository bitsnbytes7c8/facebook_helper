import message_senders;
import sys;

senders = {};

#Calls message_senders with start and end indices to get all message senders and writes their ids and names to a file "outfile"
def get_senders(filename):
  f = open(filename, "w");
  i=1;
  flag = 0;
  while(flag == 0):
    print "Querying for " + str(i) + " " + str(i+49);
    try:
      senders_dict = message_senders.get_fifty(i, i+49);
      i += 50;
      print "Received dictionary.\nProcessing....";
      if senders_dict is None:
        print "Dictionary returned is None";
        flag = 1;
        break;
      for key in senders_dict.keys():
        if key not in senders.keys():
          senders[key] = senders_dict[key];
      print "Finished processing dictionary";
    except TypeError as e:
      print "Failed to process for " + str(i) + " " + str(i+49);
      print e;
      i+=50;
      continue;
  print 'Writing to file.....';
  for key in senders.keys():
    try:
      f.write((str(senders[key]) + "\t" + str(key) + "\n").encode('utf-8'));
    except(TypeError):
      sys.stderr.write("User not found - probably a group mesg\n");
    except Exception as e:
      print e;
  return;

get_senders("outfile");
