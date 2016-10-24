import smtplib
from slacker import Slacker
from pushbullet import Pushbullet

class Notify(object):
	"""docstring for ClassName"""
	def __init__(self, order, Pushbullet_channel_Name, type_pushbullet, title, message, slack_channel, user, pwd, recipient,  dict_info = None):
		self.dict_info = dict_info
		if self.dict_info is None:
			self.order = order
			self.Pushbullet_channel_Name = Pushbullet_channel_Name
			self.type_pushbullet = type_pushbullet
			self.slack_channel = slack_channel
			self.title = title
			self.message = message
			self.user = user
			self.pwd = pwd
			self.recipient = recipient
		else:
			self.order = self.dict_info['order']
			self.Pushbullet_channel_Name = self.dict_info["Pushbullet_channel_Name"]
			self.type_pushbullet = self.dict_info['type_pushbullet']
			self.title = self.dict_info["title"]
			self.slack_channel = self.dict_info["slack_channel"]
			self.message = self.dict_info["message"]
			self.user = self.dict_info["user"]
			self.pwd = self.dict_info["pwd"]
			self.recipient = self.dict_info["recipient"]

	def _send(self, method):
		if method =="Pushbullet":
			pb = PushBulletNotification()
			if self.Pushbullet_channel_Name is None:
				return pb.note(self.title, self.message)
			else:
				return pb.channel(self.Pushbullet_channel_Name, self.type_pushbullet, self.title, self.message)
		
		if method == "Slack":
			sl = SlackerNotification()
			return sl.SlackSend(self.slack_channel, self.message)

		if method =="Email":
			return send_email(self.user, self.pwd, self.recipient, self.title, self.message)


	def Notify(self):
		sent = False
		for x in range(1,len(self.order)):
			if sent is not True:
				try:
					self._send(self.order[1])
					send = True
				except:
					if sent:
						break