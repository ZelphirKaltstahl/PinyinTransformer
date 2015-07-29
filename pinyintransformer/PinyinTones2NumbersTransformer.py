from pinyintransformer.parser.PinyinParserStrict import PinyinSyllablesParser

__author__ = 'Xiaolong'


class PinyinTones2NumbersTransformer(object):
	
	vocal_a = ['ā', 'á', 'ǎ', 'à']
	vocal_e = ['ē', 'é', 'ě', 'è']
	vocal_i = ['ī', 'í', 'ǐ', 'ì']
	vocal_o = ['ō', 'ó', 'ǒ', 'ò']
	vocal_u = ['ū', 'ú', 'ǔ', 'ù']
	vocal_ue = ['ǖ', 'ǘ', 'ǚ', 'ǜ']
	
	vocal_a_capitalized = ['Ā', 'Á', 'Ǎ', 'À']
	vocal_e_capitalized = ['Ē', 'É', 'Ě', 'È']
	vocal_i_capitalized = ['Ī', 'Í', 'Ǐ', 'Ì']
	vocal_o_capitalized = ['Ō', 'Ó', 'Ǒ', 'Ò']
	vocal_u_capitalized = ['Ū', 'Ú', 'Ǔ', 'Ù']
	vocal_ue_capitalized = ['Ǖ', 'Ǘ', 'Ǚ', 'Ǜ']
	
	all_toned_vocals = []
	all_toned_vocals.extend(vocal_a)
	all_toned_vocals.extend(vocal_e)
	all_toned_vocals.extend(vocal_i)
	all_toned_vocals.extend(vocal_o)
	all_toned_vocals.extend(vocal_u)
	all_toned_vocals.extend(vocal_ue)
	all_toned_vocals.extend(vocal_a_capitalized)
	all_toned_vocals.extend(vocal_e_capitalized)
	all_toned_vocals.extend(vocal_i_capitalized)
	all_toned_vocals.extend(vocal_o_capitalized)
	all_toned_vocals.extend(vocal_u_capitalized)
	all_toned_vocals.extend(vocal_ue_capitalized)
	
	pinyin_parser = PinyinSyllablesParser()
	
	def __init__(self):
		pass
	
	def transform(self, text="ni3hao3!"):
		
		positions_of_toned_vocals = self.getPositionsOfTonedVocals(text)
		untoned_text = self.getUntonedText(text, positions_of_toned_vocals)
		
		self.pinyin_parser.setText(untoned_text)
		self.pinyin_parser.parse()
		# print("parsing done")
		
		text_components_dict = self.pinyin_parser.getTextComponents()
		
		text_components = []
		for key in text_components_dict:
			text_components.append(text_components_dict[key])
		
		complete_pinyin_text = self.mergeTextComponentsAndToneNumbers(text_components, positions_of_toned_vocals)
		
		return complete_pinyin_text
	
	def getToneNumberOfTonedSyllable(self, syllable="zhōng"):
		
		index = self.getFirstIndexOfTonedVocal(syllable)
		
		if syllable[index] in self.vocal_a: return self.vocal_a.index(syllable[index])+1
		elif syllable[index] in self.vocal_e: return self.vocal_e.index(syllable[index])+1
		elif syllable[index] in self.vocal_i: return self.vocal_i.index(syllable[index])+1
		elif syllable[index] in self.vocal_o: return self.vocal_o.index(syllable[index])+1
		elif syllable[index] in self.vocal_u: return self.vocal_u.index(syllable[index])+1
		elif syllable[index] in self.vocal_ue: return self.vocal_ue.index(syllable[index])+1
		elif syllable[index] in self.vocal_a_capitalized: return self.vocal_a_capitalized.index(syllable[index])+1
		elif syllable[index] in self.vocal_e_capitalized: return self.vocal_e_capitalized.index(syllable[index])+1
		elif syllable[index] in self.vocal_i_capitalized: return self.vocal_i_capitalized.index(syllable[index])+1
		elif syllable[index] in self.vocal_o_capitalized: return self.vocal_o_capitalized.index(syllable[index])+1
		elif syllable[index] in self.vocal_u_capitalized: return self.vocal_u_capitalized.index(syllable[index])+1
		elif syllable[index] in self.vocal_ue_capitalized: return self.vocal_ue_capitalized.index(syllable[index])+1
		
		else:
			return 0
	
	def getFirstIndexOfTonedVocal (self, text):
		for i in range(0, len(text)):
			if text[i] in self.all_toned_vocals: return i
		return -1
	
	def getPositionsOfTonedVocals (self, text):
		result = []
		
		for i in range(0, len(text)):
			if text[i] in self.all_toned_vocals: result.append((i, self.getToneNumberOfTonedVocal(text[i])))
		
		return result
	
	def getToneNumberOfTonedVocal(self, toned_vocal):
		
		if toned_vocal in self.vocal_a: return self.vocal_a.index(toned_vocal)+1
		elif toned_vocal in self.vocal_e: return self.vocal_e.index(toned_vocal)+1
		elif toned_vocal in self.vocal_i: return self.vocal_i.index(toned_vocal)+1
		elif toned_vocal in self.vocal_o: return self.vocal_o.index(toned_vocal)+1
		elif toned_vocal in self.vocal_u: return self.vocal_u.index(toned_vocal)+1
		elif toned_vocal in self.vocal_ue: return self.vocal_ue.index(toned_vocal)+1
		elif toned_vocal in self.vocal_a_capitalized: return self.vocal_a_capitalized.index(toned_vocal)+1
		elif toned_vocal in self.vocal_e_capitalized: return self.vocal_e_capitalized.index(toned_vocal)+1
		elif toned_vocal in self.vocal_i_capitalized: return self.vocal_i_capitalized.index(toned_vocal)+1
		elif toned_vocal in self.vocal_o_capitalized: return self.vocal_o_capitalized.index(toned_vocal)+1
		elif toned_vocal in self.vocal_u_capitalized: return self.vocal_u_capitalized.index(toned_vocal)+1
		elif toned_vocal in self.vocal_ue_capitalized: return self.vocal_ue_capitalized.index(toned_vocal)+1
		
		else:
			return 0
	
	def getVocalOfTonedVocal(self, toned_vocal):
		if toned_vocal in self.vocal_a: return 'a'
		elif toned_vocal in self.vocal_e: return 'e'
		elif toned_vocal in self.vocal_i: return 'i'
		elif toned_vocal in self.vocal_o: return 'o'
		elif toned_vocal in self.vocal_u: return 'u'
		elif toned_vocal in self.vocal_ue: return 'ü'
		
		elif toned_vocal in self.vocal_a_capitalized: return 'A'
		elif toned_vocal in self.vocal_e_capitalized: return 'E'
		elif toned_vocal in self.vocal_i_capitalized: return 'I'
		elif toned_vocal in self.vocal_o_capitalized: return 'O'
		elif toned_vocal in self.vocal_u_capitalized: return 'U'
		elif toned_vocal in self.vocal_ue_capitalized: return 'Ü'
		
		else:
			return -1
	
	def getUntonedText(self, text, positions_of_toned_vocals):
		text_as_list = list(text)
		# print(positions_of_toned_vocals)
		for position in positions_of_toned_vocals:
			text_as_list[position[0]] = self.getVocalOfTonedVocal(text_as_list[position[0]])
		return "".join(text_as_list)
	
	def mergeTextComponentsAndToneNumbers(self, text_components, positions_of_toned_vocals):
		# list which saves the "index in text_components --> tone number" relation
		numbered_text_components_index = []
		
		# figure out to which text component which tone number belongs,
		# but don't add them to the text components yet, because it could
		# change the result of other iterations in this loop, if the text
		# components are suddenly longer
		for pos in positions_of_toned_vocals:
			index = self.getIndexOfTextPositionInTextComponents(pos[0], text_components)
			numbered_text_components_index.append((index, pos[1]))
		
		# change the text components according to the list of tone number
		# index in text_components relation
		for tone_number_position in numbered_text_components_index:
			text_components[tone_number_position[0]] += str(tone_number_position[1])
		
		# return everything as a string
		return "".join(text_components)
	
	@staticmethod
	def getIndexOfTextPositionInTextComponents(text_position, text_components):
		index = 0
		while text_position >= len("".join(text_components[:index+1])):
			index += 1
		return index