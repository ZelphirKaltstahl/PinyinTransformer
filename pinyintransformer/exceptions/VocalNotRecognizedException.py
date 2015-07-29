__author__ = 'Xiaolong'

class VocalNotRecognizedException(BaseException):
	def __init__(self, message):
		super(VocalNotRecognizedException, self).__init__(message)