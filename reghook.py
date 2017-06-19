from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

class StdOutListener(StreamListener):
	def on_error(self, status):
		print(status)

	def on_direct_message(self, status):
	 	print(status)       

if __name__ == '__main__':
    l = StdOutListener()
	auth = OAuthHandler('7sNaDs7hkiccidFTqDVXi1ZMW','zQC1HaCQQ0TCX5SIkCV1YkARxwFDxtIuPvCpjupigj5y4HAb2U')
	auth.set_access_token('106111046-jo87VXrNtFYZleXAbxHMOd8U94VQGU7GVO0tWjA3','GvIqG61kBQWKNUitfFwKBpgGhTOa5w1w2oxEDm5MpDnM0')
    stream = Stream(auth, l)
   