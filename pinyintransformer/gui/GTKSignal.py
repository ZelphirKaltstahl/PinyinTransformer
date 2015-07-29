__author__ = 'xiaolong'

from enum import Enum

class GTKSignal(Enum):
	CLICKED = "clicked"
	DELETE_EVENT = "delete-event"
	ACTIVATE = "activate"
	DESTROY = "destroy"