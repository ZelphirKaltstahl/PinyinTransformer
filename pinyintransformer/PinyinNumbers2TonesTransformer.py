__author__ = 'Xiaolong'

from pinyintransformer.parser.PinyinParserStrict import PinyinSyllablesParser
from pinyintransformer.exceptions.VocalNotRecognizedException import VocalNotRecognizedException

class PinyinNumbers2TonesTransformer(object):
	"""This class transforms hanyu pinyin texts like "Ni3hao3ma?" into the equivalent texts having tones instead of numbers indicating the tones."""
	
	#āáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜ
	vocals = ["a","e","i","o","u","ü"]
	vocal_a = ["ā","á","ǎ","à"]
	vocal_e = ["ē","é","ě","è"]
	vocal_i = ["ī","í","ǐ","ì"]
	vocal_o = ["ō","ó","ǒ","ò"]
	vocal_u = ["ū","ú","ǔ","ù"]
	vocal_ue = ["ǖ","ǘ","ǚ","ǜ"]
	
	#ĀÁǍÀĒÉĚÈĪÍǏÌŌÓǑÒŪÚǓÙǕǗǙǛ
	vocals_capitalized = ["A","E","I","O","U","Ü"]
	vocal_a_capitalized = ["Ā","Á","Ǎ","À"]
	vocal_e_capitalized = ["Ē","É","Ě","È"]
	vocal_i_capitalized = ["Ī","Í","Ǐ","Ì"]
	vocal_o_capitalized = ["Ō","Ó","Ǒ","Ò"]
	vocal_u_capitalized = ["Ū","Ú","Ǔ","Ù"]
	vocal_ue_capitalized = ["Ǖ","Ǘ","Ǚ","Ǜ"]
	
	#available = [ ["T" for x in initials] for y in finals]
	
	pinyin_parser = PinyinSyllablesParser()
	
	def __init__(self):
		pass
	
	def transform(self, text):
		"""This method returns the transformed pinyin text."""
		self.pinyin_parser.setText(text)
		self.pinyin_parser.parse()
		# print("parsing done")
		
		complete_pinyin_text = ""
		text_components = self.pinyin_parser.getTextComponents()
		
		for i in range(0, len(text_components)):
			if self.isPinyinSyllable(text_components[i]):
				complete_pinyin_text += self.getTonedSyllableFromNumberedSyllable(text_components[i])
			else:
				complete_pinyin_text += str(text_components[i])
		
		return complete_pinyin_text

	@staticmethod
	def getToneNumberOfSyllable(syllable):
		"""Returns the tone number of a given syllable. If not tone number is found, 0 is returned."""
		# the default value is 0, stands for no tone
		if syllable[-1] == '1': return 1
		elif syllable[-1] == '2': return 2
		elif syllable[-1] == '3': return 3
		elif syllable[-1] == '4': return 4
		else:
			return 0

	def getTonedVocals(self, vocals, tone_numbers):
		"""Returns the given vocal with the tone which is indicated by the given tone number."""
		toned_vocals = []
		for i in range(0, len(vocals)):
			toned_vocals.append(self.getTonedVocalFromVocalAndToneNumber(vocals[i], tone_numbers[i]))
		return toned_vocals

	def getTonedVocalFromVocalAndToneNumber(self, vocal, tone_number):
		"""Returns a toned vocal. The returned tone depends on the given tone_number. For example for the vocal a will have the following return values if given the tone_numbers 1,2,3,4 --> ā,á,ǎ,à. """

		# if the tone number is 0, then the vocal will not get a tone, so it doesn't need to be changed
		if tone_number == 0:
			return vocal

		tone_number -= 1 # because array index starts at 0 but tone numbers at 1

		if vocal == 'a':
			return self.vocal_a[tone_number]
		elif vocal == 'e':
			return self.vocal_e[tone_number]
		elif vocal == 'i':
			return self.vocal_i[tone_number]
		elif vocal == 'o':
			return self.vocal_o[tone_number]
		elif vocal == 'u':
			return self.vocal_u[tone_number]
		elif vocal == 'ü':
			return self.vocal_ue[tone_number]
		elif vocal == 'A':
			return self.vocal_a_capitalized[tone_number]
		elif vocal == 'E':
			return self.vocal_e_capitalized[tone_number]
		elif vocal == 'I':
			return self.vocal_i_capitalized[tone_number]
		elif vocal == 'O':
			return self.vocal_o_capitalized[tone_number]
		elif vocal == 'U':
			return self.vocal_u_capitalized[tone_number]
		elif vocal == 'Ü':
			return self.vocal_ue_capitalized[tone_number]
		else:
			raise VocalNotRecognizedException("Vocal expected but different letter received.")

	def getTonedSyllables(self, syllables):
		"""
		:param syllables: a list of syllables
		:type syllables: list
		:return: a list of syllables which have their vocals changed according to their tone numbers 
		"""
		toned_syllables = []

		for i in range(0, len(syllables)):

			#tone_number = self.getToneNumberOfSyllable(syllables[i])

			toned_syllables.append(
				self.removeToneNumbersFromText(
					self.getTonedSyllableFromNumberedSyllable(syllables[i])
				)
			)

		return toned_syllables

	def getTonedSyllableFromSyllableAndToneNumber(self, syllable, tone_number):
		"""
		(1) A and e trump all other vowels and always take the tone mark. There are no Mandarin syllables in Hanyu Pinyin that contain both a and e.
		(2) In the combination ou, o takes the mark.
		(3) In all other cases, the final vowel takes the mark.
		"""

		# (1) A and e trump all other vowels and always take the tone mark. There are no Mandarin syllables in Hanyu Pinyin that contain both a and e.
		if 'a' in syllable:
			return syllable.replace('a', self.getTonedVocalFromVocalAndToneNumber('a', tone_number))
		elif 'A' in syllable:
			return syllable.replace('A', self.getTonedVocalFromVocalAndToneNumber('A', tone_number))

		# (1) A and e trump all other vowels and always take the tone mark. There are no Mandarin syllables in Hanyu Pinyin that contain both a and e.
		elif 'e' in syllable:
			return syllable.replace('e', self.getTonedVocalFromVocalAndToneNumber('e', tone_number))
		elif 'E' in syllable:
			return syllable.replace('E', self.getTonedVocalFromVocalAndToneNumber('E', tone_number))
		
		# (2) In the combination ou, o takes the mark.
		elif 'ou' in syllable:
			return syllable.replace("o", self.getTonedVocalFromVocalAndToneNumber('o', tone_number))
		elif 'Ou' in syllable:
			return syllable.replace("O", self.getTonedVocalFromVocalAndToneNumber('O', tone_number))
		elif 'OU' in syllable:
			return syllable.replace("O", self.getTonedVocalFromVocalAndToneNumber('O', tone_number))
		# (3) In all other cases, the final vowel takes the mark.
		else:
			# print("Syllable", syllable)
			last_vocal = self.getLastVocal(syllable)
			return syllable.replace(last_vocal, self.getTonedVocalFromVocalAndToneNumber(last_vocal, tone_number))

	def getTonedSyllableFromNumberedSyllable(self, numbered_syllable):
		"""
		(1) A and e trump all other vowels and always take the tone mark. There are no Mandarin syllables in Hanyu Pinyin that contain both a and e.
		(2) In the combination ou, o takes the mark.
		(3) In all other cases, the final vowel takes the mark.
		"""
		plain_syllable = numbered_syllable
		tone_number = self.getToneNumberOfSyllable(numbered_syllable)
		if numbered_syllable[-1] in ['0','1','2','3','4']:
			plain_syllable = numbered_syllable[:-1]
		
		# (1) A and e trump all other vowels and always take the tone mark. There are no Mandarin syllables in Hanyu Pinyin that contain both a and e.
		if 'a' in plain_syllable:
			return plain_syllable.replace('a', self.getTonedVocalFromVocalAndToneNumber('a', tone_number))
		elif 'A' in plain_syllable:
			return plain_syllable.replace('A', self.getTonedVocalFromVocalAndToneNumber('A', tone_number))

		# (1) A and e trump all other vowels and always take the tone mark. There are no Mandarin syllables in Hanyu Pinyin that contain both a and e.
		elif 'e' in plain_syllable:
			return plain_syllable.replace('e', self.getTonedVocalFromVocalAndToneNumber('e', tone_number))
		elif 'E' in plain_syllable:
			return plain_syllable.replace('E', self.getTonedVocalFromVocalAndToneNumber('E', tone_number))
		
		# (2) In the combination ou, o takes the mark.
		elif 'ou' in plain_syllable:
			return plain_syllable.replace("o", self.getTonedVocalFromVocalAndToneNumber('o', tone_number))
		elif 'Ou' in plain_syllable:
			return plain_syllable.replace("O", self.getTonedVocalFromVocalAndToneNumber('O', tone_number))
		elif 'OU' in plain_syllable:
			return plain_syllable.replace("O", self.getTonedVocalFromVocalAndToneNumber('O', tone_number))
		# (3) In all other cases, the final vowel takes the mark.
		else:
			# print("Plain Syllable", plain_syllable)
			last_vocal = self.getLastVocal(plain_syllable)
			return plain_syllable.replace(last_vocal, self.getTonedVocalFromVocalAndToneNumber(last_vocal, tone_number))

	def getLastVocal(self, syllable):
		""" This method finds and returns the last vocal of a given syllable. """
		maximum_index = -1
		for i in range(0, len(self.vocals)):
			maximum_index = max(
				[maximum_index, syllable.rfind(self.vocals[i])]
			)
		# print("maximum index:", maximum_index)
		# print("syllable:", syllable)
		return syllable[maximum_index]

	@staticmethod
	def removeToneNumbersFromText(text):
		""" Removes the tone number from a syllable. """
		return ''.join([i for i in text if not i.isdigit()])

	def isPinyinSyllable(self, text):
		""" This method checks whether a given string is a hanyu pinyin syllable. """
		return self.pinyin_parser.isPinyinSyllable(text)