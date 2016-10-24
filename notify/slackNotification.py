from slacker import Slacker

class SlackerNotification(object):
	"""docstring for SlackerNotification"""
	def __init__(self, api):
		self.api = api
		self.slack = Slacker(self.api)

	def SlackSend(self, channel, message):
		self.slack.chat.post_message(channel, message)

