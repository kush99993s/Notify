from slacker import Slacker

class SlackerNotification(object):
	"""docstring for SlackerNotification"""
	def __init__(self, api ="xoxp-94935826689-94935826785-94908656083-7110a865d090809f0781b18c462dff52"):
		self.api = api
		self.slack = Slacker(self.api)

	def SlackSend(self, channel, message):
		self.slack.chat.post_message(channel, message)

