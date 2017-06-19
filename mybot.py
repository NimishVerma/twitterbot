import tweepy
auth = tweepy.OAuthHandler('7sNaDs7hkiccidFTqDVXi1ZMW','zQC1HaCQQ0TCX5SIkCV1YkARxwFDxtIuPvCpjupigj5y4HAb2U')
auth.set_access_token('106111046-jo87VXrNtFYZleXAbxHMOd8U94VQGU7GVO0tWjA3','GvIqG61kBQWKNUitfFwKBpgGhTOa5w1w2oxEDm5MpDnM0')
api = tweepy.API(auth)
user = api.get_user('twitter')
lt = api.direct_messages()[0]
message=lt.text 
sender_id=lt.sender_id
if message:
	api.send_direct_message('sender_id',text='message')