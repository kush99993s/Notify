from pushbullet import Pushbullet

class PushBulletNotification(object):
	"""docstring for ClassName"""
	def __init__(self, api_key = "o.rsapwRyLZqYQZIM5mEZ3VACIowv4top1" ):
		self.api_key = api_key
		self.pb = Pushbullet(self.api_key)		


	def note(self, title, message):
		try:
			return self.pb.push_note(title, message)
		except(Exception, e):
			return "Error"
		
	def channel(self, channel_Name, type, title, message):
		index = 0
		for channel in pb.channels:
			if channel.name == channel_Name:
				break
			else:
				index += 1

		if channel.name == channel_Name:
			my_channel = self.pb.channels[index]
			my_channel.push_note(title, message)
		else:
			return self.note("could not find channel" + title, message)