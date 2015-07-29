from enum import Enum
from pinyintransformer.parser.SpecialCharacters import SpecialCharacters

__author__ = 'xiaolong'

class PinyinOperations(Enum):
	
	@staticmethod
	def getAllNumberedVariantsOfPlainSyllable(plain_syllable):
		"""returns all numbered variants of a syllable"""
		return [
			plain_syllable[0].lower() + plain_syllable[1:] + str(0),
			plain_syllable[0].lower() + plain_syllable[1:] + str(1),
			plain_syllable[0].lower() + plain_syllable[1:] + str(2),
			plain_syllable[0].lower() + plain_syllable[1:] + str(3),
			plain_syllable[0].lower() + plain_syllable[1:] + str(4),
			plain_syllable[0].upper() + plain_syllable[1:] + str(0),
			plain_syllable[0].upper() + plain_syllable[1:] + str(1),
			plain_syllable[0].upper() + plain_syllable[1:] + str(2),
			plain_syllable[0].upper() + plain_syllable[1:] + str(3),
			plain_syllable[0].upper() + plain_syllable[1:] + str(4)
		]
	
	def getAllTonedVariantsOfPlainSyllable(self, plain_syllable):
		"""returns all toned variants of a syllable"""
		return [
			self.getTonedSyllableFromPlainSyllableAndToneNumber(plain_syllable[0].lower() + plain_syllable[1:], 1),
			self.getTonedSyllableFromPlainSyllableAndToneNumber(plain_syllable[0].lower() + plain_syllable[1:], 2),
			self.getTonedSyllableFromPlainSyllableAndToneNumber(plain_syllable[0].lower() + plain_syllable[1:], 3),
			self.getTonedSyllableFromPlainSyllableAndToneNumber(plain_syllable[0].lower() + plain_syllable[1:], 4),
			
			self.getTonedSyllableFromPlainSyllableAndToneNumber(plain_syllable[0].upper() + plain_syllable[1:], 1),
			self.getTonedSyllableFromPlainSyllableAndToneNumber(plain_syllable[0].upper() + plain_syllable[1:], 2),
			self.getTonedSyllableFromPlainSyllableAndToneNumber(plain_syllable[0].upper() + plain_syllable[1:], 3),
			self.getTonedSyllableFromPlainSyllableAndToneNumber(plain_syllable[0].upper() + plain_syllable[1:], 4)
		]
	
	def getAllVariantsOfPlainSyllable(self, plain_syllable):
		"""returns all variants of a syllable"""
		return [
			plain_syllable[0].lower() + plain_syllable[1:],
			plain_syllable[0].upper() + plain_syllable[1:],
			
			plain_syllable[0].lower() + plain_syllable[1:] + str(0),
			plain_syllable[0].lower() + plain_syllable[1:] + str(1),
			plain_syllable[0].lower() + plain_syllable[1:] + str(2),
			plain_syllable[0].lower() + plain_syllable[1:] + str(3),
			plain_syllable[0].lower() + plain_syllable[1:] + str(4),
			
			plain_syllable[0].upper() + plain_syllable[1:] + str(0),
			plain_syllable[0].upper() + plain_syllable[1:] + str(1),
			plain_syllable[0].upper() + plain_syllable[1:] + str(2),
			plain_syllable[0].upper() + plain_syllable[1:] + str(3),
			plain_syllable[0].upper() + plain_syllable[1:] + str(4),
			
			self.getTonedSyllableFromPlainSyllableAndToneNumber(plain_syllable[0].lower() + plain_syllable[1:], 1),
			self.getTonedSyllableFromPlainSyllableAndToneNumber(plain_syllable[0].lower() + plain_syllable[1:], 2),
			self.getTonedSyllableFromPlainSyllableAndToneNumber(plain_syllable[0].lower() + plain_syllable[1:], 3),
			self.getTonedSyllableFromPlainSyllableAndToneNumber(plain_syllable[0].lower() + plain_syllable[1:], 4),
			
			self.getTonedSyllableFromPlainSyllableAndToneNumber(plain_syllable[0].upper() + plain_syllable[1:], 1),
			self.getTonedSyllableFromPlainSyllableAndToneNumber(plain_syllable[0].upper() + plain_syllable[1:], 2),
			self.getTonedSyllableFromPlainSyllableAndToneNumber(plain_syllable[0].upper() + plain_syllable[1:], 3),
			self.getTonedSyllableFromPlainSyllableAndToneNumber(plain_syllable[0].upper() + plain_syllable[1:], 4)
		]
	
	@staticmethod
	def getAllPlainVariantsOfPlainSyllable(plain_syllable):
		return [
			plain_syllable[0].lower() + plain_syllable[1:],
			plain_syllable[0].upper() + plain_syllable[1:]
		]
	
	def isPinyinSyllable(self, text):
		"""returns true if the given text is a valid pinyin syllable"""
		for plain_syllable in SpecialCharacters.POSSIBLE_PLAIN_PINYIN_SYLLABLES.value:
			if text in self.getAllPlainVariantsOfPlainSyllable(plain_syllable):
				return True
			elif text in self.getAllNumberedVariantsOfPlainSyllable(plain_syllable):
				return True
			elif text in self.getAllTonedVariantsOfPlainSyllable(plain_syllable):
				return True
		return False
	
	