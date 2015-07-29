__author__ = 'Xiaolong'

class PinyinParseException(BaseException):
	def __init__(self, message):
		super(PinyinParseException, self).__init__(message)