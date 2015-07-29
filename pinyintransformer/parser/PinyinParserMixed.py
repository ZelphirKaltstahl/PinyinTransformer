from pinyintransformer.exceptions.PinyinParseException import PinyinParseException
from pinyintransformer.exceptions.VocalNotRecognizedException import VocalNotRecognizedException
# from pinyintransformer.parser.SpecialCharacters import SpecialCharacters

__author__ = 'xiaolong'
"""

(0) Enthaelt der Text ignorable characters, dann merke diese als TextComponents
(1) Pruefe ob der Text am Anfang eine PinyinSilbe enthaelt egal ob mit oder ohne Ton
	(1.1) Schaue fuer jede Silbe in jedem Ton nach ob sie am Anfang steht oder nicht.
		(1.1.1) Zum Beispiel: yin yin1 yin2 yin3 yin4 yin yīn yín yǐn yìn (10 Tests pro Silbe --> 10x so lange wie bisher)
	(1.2) Falls etwas enthalten ist schaue ob noch laengere Silben enthalten sind, dann merke die laengste als text component
(2) Nimm die Silbe vom Text weg.
(3) Fahre so fort bis alle Silben als Text Components gespeichert sind.
(4) Wandle dann erst die einzelnen Text Components um
(5) Setze den Text zusammen.

IDEE: Bedingter Einsatz des Mixed Parsers: Nur falls im TonenFeld Zahlen enthalten sind oder im NumberFeld irgendwelche betonten Vokale entahlten sind.
Ansonsten Strict Parser nehmen.

"""

class PinyinParserMixed(object):

	TONE_NUMBERS = ["0", "1", "2", "3", "4"]
	
	IGNORABLE_CHARACTERS = [
		'.', ',', '?', '!', ':', '-', ';', '…', '·', '–', '~',
		'。', '，', '、', '？', '！',
		'\"', '\'', '“', '”', '‘', '’', '´', '`',
		'/','\\',
		'(',')','[',']','{','}',
		' ',
		'\n','\t'
	]
	
	OTHER_DIGITS = ["5", "6", "7", "8", "9"]
	
	VOWELS = ["a","e","i","o","u","ü"]
	VOWELS_A = ["ā","á","ǎ","à"]
	VOWELS_E = ["ē","é","ě","è"]
	VOWELS_I = ["ī","í","ǐ","ì"]
	VOWELS_O = ["ō","ó","ǒ","ò"]
	VOWELS_U = ["ū","ú","ǔ","ù"]
	VOWELS_UE = ["ǖ","ǘ","ǚ","ǜ"]
	
	VOCALS_CAPITALIZED = ["A","E","I","O","U","Ü"]
	VOCAL_A_CAPITALIZED = ["Ā","Á","Ǎ","À"]
	VOCAL_E_CAPITALIZED = ["Ē","É","Ě","È"]
	VOCAL_I_CAPITALIZED = ["Ī","Í","Ǐ","Ì"]
	VOCAL_O_CAPITALIZED = ["Ō","Ó","Ǒ","Ò"]
	VOCAL_U_CAPITALIZED = ["Ū","Ú","Ǔ","Ù"]
	VOCAL_UE_CAPITALIZED = ["Ǖ","Ǘ","Ǚ","Ǜ"]
	
	TONED_VOWELS = [
		"Ā","Á","Ǎ","À",
		"Ē","É","Ě","È",
		"Ī","Í","Ǐ","Ì",
		"Ō","Ó","Ǒ","Ò",
		"Ū","Ú","Ǔ","Ù",
		"Ǖ","Ǘ","Ǚ","Ǜ",
		"ā","á","ǎ","à",
		"ē","é","ě","è",
		"ī","í","ǐ","ì",
		"ō","ó","ǒ","ò",
		"ū","ú","ǔ","ù",
		"ǖ","ǘ","ǚ","ǜ"
	]
	
	POSSIBLE_PLAIN_PINYIN_SYLLABLES_DICTIONARY = {
		"zhi":True,"chi":True,"shi":True,"ri":True,"zi":True,"ci":True,"si":True,
		"a":True,"ba":True,"pa":True,"ma":True,"fa":True,"da":True,"ta":True,"na":True,"la":True,"ga":True,"ka":True,"ha":True,"zha":True,"cha":True,"sha":True,"za":True,"ca":True,"sa":True,
		"o":True,"bo":True,"po":True,"mo":True,"fo":True,"lo":True,
		"e":True,"me":True,"de":True,"te":True,"ne":True,"le":True,"ge":True,"ke":True,"he":True,"zhe":True,"che":True,"she":True,"re":True,"ze":True,"ce":True,"se":True,
		"ai":True,"bai":True,"pai":True,"mai":True,"dai":True,"tai":True,"nai":True,"lai":True,"gai":True,"kai":True,"hai":True,"zhai":True,"chai":True,"shai":True,"zai":True,"cai":True,"sai":True,
		"ei":True,"bei":True,"pei":True,"mei":True,"fei":True,"dei":True,"tei":True,"nei":True,"lei":True,"gei":True,"kei":True,"hei":True,"zhei":True,"shei":True,"zei":True,"sei":True,
		"ao":True,"bao":True,"pao":True,"mao":True,"dao":True,"tao":True,"nao":True,"lao":True,"gao":True,"kao":True,"hao":True,"zhao":True,"chao":True,"shao":True,"rao":True,"zao":True,"cao":True,"sao":True,
		"ou":True,"pou":True,"mou":True,"fou":True,"dou":True,"tou":True,"nou":True,"lou":True,"gou":True,"kou":True,"hou":True,"zhou":True,"chou":True,"shou":True,"rou":True,"zou":True,"cou":True,"sou":True,
		"an":True,"ban":True,"pan":True,"man":True,"fan":True,"dan":True,"tan":True,"nan":True,"lan":True,"gan":True,"kan":True,"han":True,"zhan":True,"chan":True,"shan":True,"ran":True,"zan":True,"can":True,"san":True,
		"en":True,"ben":True,"pen":True,"men":True,"fen":True,"den":True,"nen":True,"gen":True,"ken":True,"hen":True,"zhen":True,"chen":True,"shen":True,"ren":True,"zen":True,"cen":True,"sen":True,
		"ang":True,"bang":True,"pang":True,"mang":True,"fang":True,"dang":True,"tang":True,"nang":True,"lang":True,"gang":True,"kang":True,"hang":True,"zhang":True,"chang":True,"shang":True,"rang":True,"zang":True,"cang":True,"sang":True,
		"eng":True,"beng":True,"peng":True,"meng":True,"feng":True,"deng":True,"teng":True,"neng":True,"leng":True,"geng":True,"keng":True,"heng":True,"zheng":True,"cheng":True,"sheng":True,"reng":True,"zeng":True,"ceng":True,"seng":True,
		"er":True,
		"yi":True,"bi":True,"pi":True,"mi":True,"di":True,"ti":True,"ni":True,"li":True,"ji":True,"qi":True,"xi":True,
		"ya":True,"dia":True,"nia":True,"lia":True,"jia":True,"qia":True,"xia":True,
		"yo":True,
		"ye":True,"bie":True,"pie":True,"mie":True,"die":True,"tie":True,"nie":True,"lie":True,"jie":True,"qie":True,"xie":True,
		"yai":True,
		"yao":True,"biao":True,"piao":True,"miao":True,"fiao":True,"diao":True,"tiao":True,"niao":True,"liao":True,"jiao":True,"qiao":True,"xiao":True,
		"you":True,"miu":True,"diu":True,"niu":True,"liu":True,"jiu":True,"qiu":True,"xiu":True,
		"yan":True,"bian":True,"pian":True,"mian":True,"dian":True,"tian":True,"nian":True,"lian":True,"jian":True,"qian":True,"xian":True,
		"yin":True,"bin":True,"pin":True,"min":True,"nin":True,"lin":True,"jin":True,"qin":True,"xin":True,
		"yang":True,"biang":True,"diang":True,"niang":True,"liang":True,"jiang":True,"qiang":True,"xiang":True,
		"ying":True,"bing":True,"ping":True,"ming":True,"ding":True,"ting":True,"ning":True,"ling":True,"jing":True,"qing":True,"xing":True,
		"wu":True,"bu":True,"pu":True,"mu":True,"fu":True,"du":True,"tu":True,"nu":True,"lu":True,"gu":True,"ku":True,"hu":True,"zhu":True,"chu":True,"shu":True,"ru":True,"zu":True,"cu":True,"su":True,
		"wa":True,"gua":True,"kua":True,"hua":True,"zhua":True,"chua":True,"shua":True,"rua":True,
		"wo":True,"duo":True,"tuo":True,"nuo":True,"luo":True,"guo":True,"kuo":True,"huo":True,"zhuo":True,"chuo":True,"shuo":True,"ruo":True,"zuo":True,"cuo":True,"suo":True,
		"wai":True,"guai":True,"kuai":True,"huai":True,"zhuai":True,"chuai":True,"shuai":True,
		"wei":True,"dui":True,"tui":True,"gui":True,"kui":True,"hui":True,"zhui":True,"chui":True,"shui":True,"rui":True,"zui":True,"cui":True,"sui":True,
		"wan":True,"duan":True,"tuan":True,"nuan":True,"luan":True,"guan":True,"kuan":True,"huan":True,"zhuan":True,"chuan":True,"shuan":True,"ruan":True,"zuan":True,"cuan":True,"suan":True,
		"wen":True,"dun":True,"tun":True,"nun":True,"lun":True,"gun":True,"kun":True,"hun":True,"zhun":True,"chun":True,"shun":True,"run":True,"zun":True,"cun":True,"sun":True,
		"wang":True,"guang":True,"kuang":True,"huang":True,"zhuang":True,"chuang":True,"shuang":True,
		"weng":True,"dong":True,"tong":True,"nong":True,"long":True,"gong":True,"kong":True,"hong":True,"zhong":True,"chong":True,"shong":True,"rong":True,"zong":True,"cong":True,"song":True,
		"yu":True,"nü":True,"lü":True,"ju":True,"qu":True,"xu":True,
		"yue":True,"nüe":True,"lüe":True,"jue":True,"que":True,"xue":True,
		"yuan":True,"juan":True,"quan":True,"xuan":True,
		"yun":True,"lün":True,"jun":True,"qun":True,"xun":True,
		"yong":True,"jiong":True,"qiong":True,"xiong":True
	}
	
	POSSIBLE_PLAIN_PINYIN_SYLLABLES = [
		"zhi","chi","shi","ri","zi","ci","si",
		"a","ba","pa","ma","fa","da","ta","na","la","ga","ka","ha","zha","cha","sha","za","ca","sa",
		"o","bo","po","mo","fo","lo",
		"e","me","de","te","ne","le","ge","ke","he","zhe","che","she","re","ze","ce","se",
		"ai","bai","pai","mai","dai","tai","nai","lai","gai","kai","hai","zhai","chai","shai","zai","cai","sai",
		"ei","bei","pei","mei","fei","dei","tei","nei","lei","gei","kei","hei","zhei","shei","zei","sei",
		"ao","bao","pao","mao","dao","tao","nao","lao","gao","kao","hao","zhao","chao","shao","rao","zao","cao","sao",
		"ou","pou","mou","fou","dou","tou","nou","lou","gou","kou","hou","zhou","chou","shou","rou","zou","cou","sou",
		"an","ban","pan","man","fan","dan","tan","nan","lan","gan","kan","han","zhan","chan","shan","ran","zan","can","san",
		"en","ben","pen","men","fen","den","nen","gen","ken","hen","zhen","chen","shen","ren","zen","cen","sen",
		"ang","bang","pang","mang","fang","dang","tang","nang","lang","gang","kang","hang","zhang","chang","shang","rang","zang","cang","sang",
		"eng","beng","peng","meng","feng","deng","teng","neng","leng","geng","keng","heng","zheng","cheng","sheng","reng","zeng","ceng","seng",
		"er",
		"yi","bi","pi","mi","di","ti","ni","li","ji","qi","xi",
		"ya","dia","nia","lia","jia","qia","xia",
		"yo",
		"ye","bie","pie","mie","die","tie","nie","lie","jie","qie","xie",
		"yai",
		"yao","biao","piao","miao","fiao","diao","tiao","niao","liao","jiao","qiao","xiao",
		"you","miu","diu","niu","liu","jiu","qiu","xiu",
		"yan","bian","pian","mian","dian","tian","nian","lian","jian","qian","xian",
		"yin","bin","pin","min","nin","lin","jin","qin","xin",
		"yang","biang","diang","niang","liang","jiang","qiang","xiang",
		"ying","bing","ping","ming","ding","ting","ning","ling","jing","qing","xing",
		"wu","bu","pu","mu","fu","du","tu","nu","lu","gu","ku","hu","zhu","chu","shu","ru","zu","cu","su",
		"wa","gua","kua","hua","zhua","chua","shua","rua",
		"wo","duo","tuo","nuo","luo","guo","kuo","huo","zhuo","chuo","shuo","ruo","zuo","cuo","suo",
		"wai","guai","kuai","huai","zhuai","chuai","shuai",
		"wei","dui","tui","gui","kui","hui","zhui","chui","shui","rui","zui","cui","sui",
		"wan","duan","tuan","nuan","luan","guan","kuan","huan","zhuan","chuan","shuan","ruan","zuan","cuan","suan",
		"wen","dun","tun","nun","lun","gun","kun","hun","zhun","chun","shun","run","zun","cun","sun",
		"wang","guang","kuang","huang","zhuang","chuang","shuang",
		"weng","dong","tong","nong","long","gong","kong","hong","zhong","chong","shong","rong","zong","cong","song",
		"yu","nü","lü","ju","qu","xu",
		"yue","nüe","lüe","jue","que","xue",
		"yuan","juan","quan","xuan",
		"yun","lün","jun","qun","xun",
		"yong","jiong","qiong","xiong"
	]
	
	text_components = None
	is_text_component_plain_syllable_dictionary = None
	is_text_component_numbered_syllable_dictionary = None
	is_text_component_toned_syllable_dictionary = None
	
	def __init__(self):
		self.text_components = []
		self.is_text_component_plain_syllable_dictionary = {}
		self.is_text_component_numbered_syllable_dictionary = {}
		self.is_text_component_toned_syllable_dictionary = {}
		
	def parse(self, pinyin_text):
		"""
		returns the components of the text
		"""
		
		self.text_components = []
		
		self.is_text_component_plain_syllable_dictionary = {}
		self.is_text_component_numbered_syllable_dictionary = {}
		self.is_text_component_toned_syllable_dictionary = {}
		
		longest_matching_syllable_found = ""
		
		is_plain_syllable = False
		is_numbered_syllable = False
		is_toned_syllable = False
		
		pinyin_text = self.removeValidNonSyllableCharacters(pinyin_text)
		
		while len(pinyin_text) > 0:
			for plain_syllable in self.POSSIBLE_PLAIN_PINYIN_SYLLABLES: 
				
				for syllable_variant in self.getNumberedVariantsOfPlainSyllable(plain_syllable): # x10
					
					if (pinyin_text.find(syllable_variant) == 0) and (len(syllable_variant) > len(longest_matching_syllable_found)):
						is_toned_syllable = False
						is_numbered_syllable = True
						is_plain_syllable = False
						longest_matching_syllable_found = syllable_variant
				
				if not is_numbered_syllable: # if a syllable ending with a number has been found, there cannot be any plain syllable matching
				
					for syllable_variant in self.getPlainVariantsOfPlainSyllable(plain_syllable): # x2
						
						if (pinyin_text.find(syllable_variant) == 0) and (len(syllable_variant) > len(longest_matching_syllable_found)):
							is_toned_syllable = False
							is_numbered_syllable = False
							is_plain_syllable = True
							longest_matching_syllable_found = syllable_variant
						
						
				if not is_numbered_syllable: # if a syllable ending with a number has been found, there cannot be any toned syllable matching
					
					for syllable_variant in self.getTonedVariantsOfPlainSyllable(plain_syllable): # x8
						
						if (pinyin_text.find(syllable_variant) == 0) and (len(syllable_variant) > len(longest_matching_syllable_found)):
							is_toned_syllable = True
							is_numbered_syllable = False
							is_plain_syllable = False
							longest_matching_syllable_found = syllable_variant
					
			
			if (len(pinyin_text) > 0) and (longest_matching_syllable_found == ""):
				raise PinyinParseException(
					"".join([
						"Invalid pinyin input: \n",
						"Remaining text:|", pinyin_text, "|\n",
						"Longest syllable length:|", str(len(longest_matching_syllable_found)), "|\n",
						"Longest syllable fitting:|", longest_matching_syllable_found, "|"
					])
				)
			
			else:
				pinyin_text = pinyin_text[len(longest_matching_syllable_found):]
								
				if is_plain_syllable:
					self.addPlainSyllableToTextComponents(longest_matching_syllable_found)
				elif is_numbered_syllable:
					self.addNumberedSyllableToTextComponents(longest_matching_syllable_found)
				elif is_toned_syllable:
					self.addTonedSyllableToTextComponents(longest_matching_syllable_found)
				else:
					raise PinyinParseException(
						"".join([
							"Invalid pinyin input: \n",
							"Remaining text:|", pinyin_text, "|\n",
							"Longest syllable length:|", str(len(longest_matching_syllable_found)), "|\n",
							"Longest syllable fitting:|", longest_matching_syllable_found, "|"
						])
					)
				
				pinyin_text = self.removeValidNonSyllableCharacters(pinyin_text)

				# reset values
				longest_matching_syllable_found = ""
				is_plain_syllable = False
				is_numbered_syllable = False
				is_toned_syllable = False
		
		return self.text_components
	
	@staticmethod
	def getNumberedVariantsOfPlainSyllable(plain_syllable):
		"""returns all numbered variants of a syllable"""
		return [
			"".join([plain_syllable[0].lower(), plain_syllable[1:], str(0)]),
			"".join([plain_syllable[0].lower(), plain_syllable[1:], str(1)]),
			"".join([plain_syllable[0].lower(), plain_syllable[1:], str(2)]),
			"".join([plain_syllable[0].lower(), plain_syllable[1:], str(3)]),
			"".join([plain_syllable[0].lower(), plain_syllable[1:], str(4)]),
			"".join([plain_syllable[0].upper(), plain_syllable[1:], str(0)]),
			"".join([plain_syllable[0].upper(), plain_syllable[1:], str(1)]),
			"".join([plain_syllable[0].upper(), plain_syllable[1:], str(2)]),
			"".join([plain_syllable[0].upper(), plain_syllable[1:], str(3)]),
			"".join([plain_syllable[0].upper(), plain_syllable[1:], str(4)])
		]
	
	def getTonedVariantsOfPlainSyllable(self, plain_syllable):
		"""returns all toned variants of a syllable"""
		return [
			self.getTonedSyllableFromPlainSyllableAndToneNumber("".join([plain_syllable[0].lower(), plain_syllable[1:]]), 1),
			self.getTonedSyllableFromPlainSyllableAndToneNumber("".join([plain_syllable[0].lower(), plain_syllable[1:]]), 2),
			self.getTonedSyllableFromPlainSyllableAndToneNumber("".join([plain_syllable[0].lower(), plain_syllable[1:]]), 3),
			self.getTonedSyllableFromPlainSyllableAndToneNumber("".join([plain_syllable[0].lower(), plain_syllable[1:]]), 4),
			
			self.getTonedSyllableFromPlainSyllableAndToneNumber("".join([plain_syllable[0].upper(), plain_syllable[1:]]), 1),
			self.getTonedSyllableFromPlainSyllableAndToneNumber("".join([plain_syllable[0].upper(), plain_syllable[1:]]), 2),
			self.getTonedSyllableFromPlainSyllableAndToneNumber("".join([plain_syllable[0].upper(), plain_syllable[1:]]), 3),
			self.getTonedSyllableFromPlainSyllableAndToneNumber("".join([plain_syllable[0].upper(), plain_syllable[1:]]), 4)
		]
	
	def getAllVariantsOfPlainSyllable(self, plain_syllable):
		"""returns all variants of a syllable"""
		return [
			"".join([plain_syllable[0].lower(), plain_syllable[1:]]),
			"".join([plain_syllable[0].upper(), plain_syllable[1:]]),
			
			"".join([plain_syllable[0].lower(), plain_syllable[1:], str(0)]),
			"".join([plain_syllable[0].lower(), plain_syllable[1:], str(1)]),
			"".join([plain_syllable[0].lower(), plain_syllable[1:], str(2)]),
			"".join([plain_syllable[0].lower(), plain_syllable[1:], str(3)]),
			"".join([plain_syllable[0].lower(), plain_syllable[1:], str(4)]),
			
			"".join([plain_syllable[0].upper(), plain_syllable[1:], str(0)]),
			"".join([plain_syllable[0].upper(), plain_syllable[1:], str(1)]),
			"".join([plain_syllable[0].upper(), plain_syllable[1:], str(2)]),
			"".join([plain_syllable[0].upper(), plain_syllable[1:], str(3)]),
			"".join([plain_syllable[0].upper(), plain_syllable[1:], str(4)]),
			
			self.getTonedSyllableFromPlainSyllableAndToneNumber("".join([plain_syllable[0].lower(), plain_syllable[1:]]), 1),
			self.getTonedSyllableFromPlainSyllableAndToneNumber("".join([plain_syllable[0].lower(), plain_syllable[1:]]), 2),
			self.getTonedSyllableFromPlainSyllableAndToneNumber("".join([plain_syllable[0].lower(), plain_syllable[1:]]), 3),
			self.getTonedSyllableFromPlainSyllableAndToneNumber("".join([plain_syllable[0].lower(), plain_syllable[1:]]), 4),
			
			self.getTonedSyllableFromPlainSyllableAndToneNumber("".join([plain_syllable[0].upper(), plain_syllable[1:]]), 1),
			self.getTonedSyllableFromPlainSyllableAndToneNumber("".join([plain_syllable[0].upper(), plain_syllable[1:]]), 2),
			self.getTonedSyllableFromPlainSyllableAndToneNumber("".join([plain_syllable[0].upper(), plain_syllable[1:]]), 3),
			self.getTonedSyllableFromPlainSyllableAndToneNumber("".join([plain_syllable[0].upper(), plain_syllable[1:]]), 4)
		]
	
	@staticmethod
	def getPlainVariantsOfPlainSyllable(plain_syllable):
		return [
			"".join([plain_syllable[0].lower(), plain_syllable[1:]]),
			"".join([plain_syllable[0].upper(), plain_syllable[1:]])
		]
	
	def isPinyinSyllable(self, text):
		# print("initial text:|", text, "|", sep="")
		text = text.lower()
		# print("text after lower:|", text, "|", sep="")
		text = self.getPlainSyllableFromTonedSyllable(text)
		# print("text after tones removed:|", text, "|", sep="")
		text = self.getPlainSyllableFromNumberedSyllable(text)
		# print("text after numbers removed:|", text, "|", sep="")
		return self.POSSIBLE_PLAIN_PINYIN_SYLLABLES_DICTIONARY.get(text, False)
		
		
		# """returns true if the given text is a valid pinyin syllable"""
		# for plain_syllable in self.POSSIBLE_PLAIN_PINYIN_SYLLABLES:
		# 	if text in self.getPlainVariantsOfPlainSyllable(plain_syllable):
		# 		return True
		# 	elif text in self.getNumberedVariantsOfPlainSyllable(plain_syllable):
		# 		return True
		# 	elif text in self.getTonedVariantsOfPlainSyllable(plain_syllable):
		# 		return True
		# return False
	
	def removeValidNonSyllableCharacters(self, text):
		"""removes all characters which are not part of a syllable"""
		
		if len(text) == 0:
			return ""
		
		while self.isValidNonSyllableCharacter(text[0]):
			self.addNonSyllableCharacterToTextComponents(text[0])
			text = text[1:]
			
			if len(text) == 0:
				return text
		
		return text
	
	def isValidNonSyllableCharacter(self, character):
		return	(character in self.IGNORABLE_CHARACTERS) or \
				(character in self.TONE_NUMBERS) or \
				(character in self.OTHER_DIGITS)
	
	def addNonSyllableCharacterToTextComponents(self, characters):
		"""adds a text component to the list of text components"""
		current_position = len(self.text_components)
		self.is_text_component_plain_syllable_dictionary[current_position] = False
		self.is_text_component_numbered_syllable_dictionary[current_position] = False
		self.is_text_component_toned_syllable_dictionary[current_position] = False
		self.text_components.append(characters)
	
	def addPlainSyllableToTextComponents(self, plain_syllable):
		# print("adding plain to position:", str(len(self.text_components)))
		current_position = len(self.text_components)
		self.is_text_component_plain_syllable_dictionary[current_position] = True
		self.is_text_component_numbered_syllable_dictionary[current_position] = False
		self.is_text_component_toned_syllable_dictionary[current_position] = False
		self.text_components.append(plain_syllable)
	
	def addNumberedSyllableToTextComponents(self, numbered_syllable):
		# print("adding numbered to position:", str(len(self.text_components)))
		current_position = len(self.text_components)
		self.is_text_component_plain_syllable_dictionary[current_position] = False
		self.is_text_component_numbered_syllable_dictionary[current_position] = True
		self.is_text_component_toned_syllable_dictionary[current_position] = False
		self.text_components.append(numbered_syllable)
	
	def addTonedSyllableToTextComponents(self, toned_syllable):
		# print("adding toned to position:", str(len(self.text_components)))
		current_position = len(self.text_components)
		self.is_text_component_plain_syllable_dictionary[current_position] = False
		self.is_text_component_numbered_syllable_dictionary[current_position] = False
		self.is_text_component_toned_syllable_dictionary[current_position] = True
		self.text_components.append(toned_syllable)
	
	def getNumberedPinyinText(self):
		"""returns the pinyin text with numbers instead of tones"""
		complete_numbered_pinyin_text = ""
		
		for i in range(0, len(self.text_components)):
			
			# print(str(len(self.text_components)))
			# print("text comp:", i)
			# 
			# print("plain dict")
			# print(self.is_text_component_plain_syllable_dictionary.items())
			# for (key, value) in self.is_text_component_plain_syllable_dictionary.items():
			# 	print(key, value)
			# 
			# print("numbered dict")
			# print(self.is_text_component_numbered_syllable_dictionary.items())
			# for (key, value) in self.is_text_component_numbered_syllable_dictionary.items():
			# 	print(key, value)
			# 
			# print("toned dict")
			# print(self.is_text_component_toned_syllable_dictionary.items())
			# for (key, value) in self.is_text_component_toned_syllable_dictionary.items():
			# 	print(key, value)
			
			if self.is_text_component_plain_syllable_dictionary[i]:
				complete_numbered_pinyin_text = "".join([complete_numbered_pinyin_text, self.text_components[i]])
			
			elif self.is_text_component_toned_syllable_dictionary[i]:
				complete_numbered_pinyin_text = "".join([complete_numbered_pinyin_text, self.getNumberedSyllableFromTonedSyllable(self.text_components[i])])
				
			elif self.is_text_component_numbered_syllable_dictionary[i]:
				complete_numbered_pinyin_text = "".join([complete_numbered_pinyin_text, self.text_components[i]])
				
			elif self.text_components[i] in self.IGNORABLE_CHARACTERS:
				complete_numbered_pinyin_text = "".join([complete_numbered_pinyin_text, self.text_components[i]])
				
			# if self.isPinyinSyllable(self.text_components[i]):
			# 	
			# 	if self.isNumberedSyllable(self.text_components[i]):
			# 		complete_numbered_pinyin_text = "".join([complete_numbered_pinyin_text, self.text_components[i]])
			# 		
			# 	elif self.isTonedSyllable(self.text_components[i]):
			# 		complete_numbered_pinyin_text = "".join([complete_numbered_pinyin_text, self.getNumberedSyllableFromTonedSyllable(self.text_components[i])])
			# 		
			# 	elif self.text_components[i].lower() in self.POSSIBLE_PLAIN_PINYIN_SYLLABLES:
			# 		complete_numbered_pinyin_text = "".join([complete_numbered_pinyin_text, self.text_components[i]])
			# 	
			# elif self.text_components[i] in self.IGNORABLE_CHARACTERS:
			# 	complete_numbered_pinyin_text = "".join([complete_numbered_pinyin_text, self.text_components[i]])
		
		return complete_numbered_pinyin_text
	
	def getTonedPinyinText(self):
		"""returns the pinyin text with numbers instead of tones"""
		complete_toned_pinyin_text = ""
		
		# for i in range(0, len(self.text_components)): # n
		# 	
		# 	if self.text_components[i].lower() in self.POSSIBLE_PLAIN_PINYIN_SYLLABLES: #
		# 			complete_toned_pinyin_text = "".join([complete_toned_pinyin_text, self.text_components[i]])
		# 	
		# 	elif self.isPinyinSyllable(self.text_components[i]): #~400x20 = 8000
		# 		
		# 		if self.isNumberedSyllable(self.text_components[i]): #+5
		# 			complete_toned_pinyin_text = "".join([complete_toned_pinyin_text, self.getTonedSyllableFromNumberedSyllable(self.text_components[i])])
		# 			
		# 		elif self.isTonedSyllable(self.text_components[i]): #+48
		# 			complete_toned_pinyin_text = "".join([complete_toned_pinyin_text, self.text_components[i]])
		# 		
		# 	elif self.text_components[i] in self.IGNORABLE_CHARACTERS:
		# 		complete_toned_pinyin_text = "".join([complete_toned_pinyin_text, self.text_components[i]])
		for i in range(0, len(self.text_components)):
			
			if self.is_text_component_plain_syllable_dictionary[i]:
				complete_toned_pinyin_text = "".join([complete_toned_pinyin_text, self.text_components[i]])
			
			elif self.is_text_component_toned_syllable_dictionary[i]:
				complete_toned_pinyin_text = "".join([complete_toned_pinyin_text, self.text_components[i]])
				
			elif self.is_text_component_numbered_syllable_dictionary[i]:
				complete_toned_pinyin_text = "".join([complete_toned_pinyin_text, self.getTonedSyllableFromNumberedSyllable(self.text_components[i])])
				
			elif self.text_components[i] in self.IGNORABLE_CHARACTERS:
				complete_toned_pinyin_text = "".join([complete_toned_pinyin_text, self.text_components[i]])
			
		return complete_toned_pinyin_text
	
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
			last_vocal = self.getLastVocalFromText(plain_syllable)
			return plain_syllable.replace(last_vocal, self.getTonedVocalFromVocalAndToneNumber(last_vocal, tone_number))
	
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
	
	def getTonedSyllableFromPlainSyllableAndToneNumber(self, plain_syllable, tone_number):
		"""
		(1) A and e trump all other vowels and always take the tone mark. There are no Mandarin syllables in Hanyu Pinyin that contain both a and e.
		(2) In the combination ou, o takes the mark.
		(3) In all other cases, the final vowel takes the mark.
		"""

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
			# print("Syllable", syllable)
			last_vocal = self.getLastVocalFromText(plain_syllable)
			return plain_syllable.replace(last_vocal, self.getTonedVocalFromVocalAndToneNumber(last_vocal, tone_number))
		
	def getNumberedSyllableFromTonedSyllable(self, toned_syllable):
		# print(toned_syllable)
		tone_number = self.getToneNumberFromTonedSyllable(toned_syllable)
		plain_syllable = self.getPlainSyllableFromTonedSyllable(toned_syllable)
		# print("plain_syllable:|",plain_syllable,"|, tone number:|",tone_number,"|", sep = "", end="\n")
		return "".join([plain_syllable, tone_number])
	
	def getTonedVocalFromVocalAndToneNumber(self, vocal, tone_number):
		"""Returns a toned vocal. The returned tone depends on the given tone_number. For example for the vocal a will have the following return values if given the tone_numbers 1,2,3,4 --> ā,á,ǎ,à. """

		# if the tone number is 0, then the vocal will not get a tone, so it doesn't need to be changed
		if tone_number == 0:
			return vocal

		tone_number -= 1 # because array index starts at 0 but tone numbers at 1

		if vocal == 'a':
			return self.VOWELS_A[tone_number]
		elif vocal == 'e':
			return self.VOWELS_E[tone_number]
		elif vocal == 'i':
			return self.VOWELS_I[tone_number]
		elif vocal == 'o':
			return self.VOWELS_O[tone_number]
		elif vocal == 'u':
			return self.VOWELS_U[tone_number]
		elif vocal == 'ü':
			return self.VOWELS_UE[tone_number]
		elif vocal == 'A':
			return self.VOCAL_A_CAPITALIZED[tone_number]
		elif vocal == 'E':
			return self.VOCAL_E_CAPITALIZED[tone_number]
		elif vocal == 'I':
			return self.VOCAL_I_CAPITALIZED[tone_number]
		elif vocal == 'O':
			return self.VOCAL_O_CAPITALIZED[tone_number]
		elif vocal == 'U':
			return self.VOCAL_U_CAPITALIZED[tone_number]
		elif vocal == 'Ü':
			return self.VOCAL_UE_CAPITALIZED[tone_number]
		else:
			raise VocalNotRecognizedException("Vocal expected but different letter received.")
		
	def getLastVocalFromText(self, syllable):
		""" This method finds and returns the last vocal of a given syllable. """
		maximum_index = -1
		for i in range(0, len(self.VOWELS)):
			maximum_index = max(
				[maximum_index, syllable.rfind(self.VOWELS[i])]
			)
		# print("maximum index:", maximum_index)
		# print("syllable:", syllable)
		return syllable[maximum_index]
	
	def isTonedSyllable (self, syllable):
		for x in self.TONED_VOWELS:
			if x in syllable:
				return True
		return False
	
	def isNumberedSyllable (self, syllable):
		for x in self.TONE_NUMBERS:
			if x in syllable:
				return True
		return False
	
	def getToneNumberFromTonedSyllable (self, toned_syllable):
		for x in range(0, len(self.TONED_VOWELS)):
			if self.TONED_VOWELS[x] in toned_syllable:
				return self.TONE_NUMBERS[(x % 4) + 1]
	
	def getPlainSyllableFromTonedSyllable (self, toned_syllable):
		toned_vocal = self.getTonedVocalOfTonedSyllable(toned_syllable)
		
		if toned_vocal in self.VOWELS_A:
			return toned_syllable.replace(toned_vocal, "a")
		elif toned_vocal in self.VOCAL_A_CAPITALIZED:
			return toned_syllable.replace(toned_vocal, "A")
		elif toned_vocal in self.VOWELS_E:
			return toned_syllable.replace(toned_vocal, "e")
		elif toned_vocal in self.VOCAL_E_CAPITALIZED:
			return toned_syllable.replace(toned_vocal, "E")
		elif toned_vocal in self.VOWELS_I:
			return toned_syllable.replace(toned_vocal, "i")
		elif toned_vocal in self.VOCAL_I_CAPITALIZED:
			return toned_syllable.replace(toned_vocal, "I")
		elif toned_vocal in self.VOWELS_O:
			return toned_syllable.replace(toned_vocal, "o")
		elif toned_vocal in self.VOCAL_O_CAPITALIZED:
			return toned_syllable.replace(toned_vocal, "O")
		elif toned_vocal in self.VOWELS_U:
			return toned_syllable.replace(toned_vocal, "u")
		elif toned_vocal in self.VOCAL_U_CAPITALIZED:
			return toned_syllable.replace(toned_vocal, "U")
		elif toned_vocal in self.VOWELS_UE:
			return toned_syllable.replace(toned_vocal, "ü")
		elif toned_vocal in self.VOCAL_UE_CAPITALIZED:
			return toned_syllable.replace(toned_vocal, "Ü")
		else:
			return toned_syllable
		
	
	def getTonedVocalOfTonedSyllable (self, toned_syllable):
		for x in toned_syllable:
			if x in self.TONED_VOWELS:
				return x
			
	def getPlainSyllableFromNumberedSyllable (self, numbered_syllable):
		if numbered_syllable[-1] in self.TONE_NUMBERS:
			return numbered_syllable[:-1]
		else:
			return numbered_syllable
	
	def fastParse(self, pinyin_text):
		
		self.text_components = []
		
		longest_pinyin_syllable_length = 7
		
		pinyin_text = self.removeValidNonSyllableCharacters(pinyin_text)
		
		while len(pinyin_text) > 0:
			
			longest_matching_syllable_found = ""
			longest_matching_syllable_found_length = 0
			number_of_characters = 1
			
			# get longest syllable which at the beginning of the text
			while number_of_characters < longest_pinyin_syllable_length:
				
				# if number_of_characters > len(pinyin_text) and longest_matching_syllable_found_length == 0:
				# 	raise PinyinParseException(
				# 	"".join([
				# 		"Invalid pinyin input: \n",
				# 		"Remaining text:|", pinyin_text, "|\n"
				# 	])
				# )
				
				if self.isPinyinSyllable(pinyin_text[:number_of_characters]):
					longest_matching_syllable_found = pinyin_text[:number_of_characters]
					longest_matching_syllable_found_length = len(longest_matching_syllable_found)
				
				number_of_characters += 1
			
			# if no syllable was found
			if longest_matching_syllable_found == "":
				raise PinyinParseException(
					"".join([
						"Invalid pinyin input: \n",
						"Remaining text:|", pinyin_text, "|\n"
					])
				)
			
			# if a syllable was found
			else:
				extracted_syllable = pinyin_text[:longest_matching_syllable_found_length]
				plain_extracted_syllable = extracted_syllable.lower()
				plain_extracted_syllable = self.getPlainSyllableFromTonedSyllable(plain_extracted_syllable)
				plain_extracted_syllable = self.getPlainSyllableFromNumberedSyllable(plain_extracted_syllable)
				
				# add plain syllable
				if longest_matching_syllable_found in self.getPlainVariantsOfPlainSyllable(plain_extracted_syllable):
					self.addPlainSyllableToTextComponents(extracted_syllable)
				
				# add numbered syllable
				elif longest_matching_syllable_found in self.getNumberedVariantsOfPlainSyllable(plain_extracted_syllable):
					self.addNumberedSyllableToTextComponents(extracted_syllable)
				
				# add toned syllable
				elif longest_matching_syllable_found in self.getTonedVariantsOfPlainSyllable(plain_extracted_syllable):
					self.addTonedSyllableToTextComponents(extracted_syllable)
			
				# delete the syllable from the pinyin text
				pinyin_text = pinyin_text[longest_matching_syllable_found_length:]
				
				# delete other chars from the pinyin text after each syllable which is deleted from it
				pinyin_text = self.removeValidNonSyllableCharacters(pinyin_text)
		
		return self.text_components