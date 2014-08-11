
#function to read access token from a file token.txt
def get_token():
  f = open("token.txt", "r");
  token = "";
  for line in f:
    token = line.strip();
    break;
  return token;
