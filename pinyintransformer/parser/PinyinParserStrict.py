__author__ = 'Xiaolong'

from pinyintransformer.exceptions.PinyinParseException import PinyinParseException

class PinyinSyllablesParser(object):

	# user input text
	text = None

	# pinyin stuff
	#initials = ["b","p","m","f","d","t","n","l","g","k","h","j","q","x","zh","ch","sh","r","z","c","s","y","w"]
	#finals = ["a","o","e","ai","ei","ao","ou","an","en","ang","eng","er","i","ia","io","ie","iai","iao","iu","ian","in","iang","ing","u","ua","uo","uai","ui","uan","un","uang","ong","ü","üe","üan","ün","iong"]
	#vocals = ["a","e","i","o","u","ü"]

	possible_pinyin_syllables = [
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

	#whitespace_characters = ['\'', '\n', '\t', ' ', '`', '´']
	#punctuation_characters = ['.', ',', '?', '!', ':', '-', ';', '\"', '/']
	#bracket_characters = ['(',')','[',']','{','}']

	ignorable_characters = [
		'.', ',', '?', '!', ':', '-', ';',
		'。', '，', '、', '？', '！',
		'\"', '\'', '“', '”', '‘', '’', '´', '`',
		'/','\\',
		'(',')','[',']','{','}',
		' ',
		'\n','\t'
	]

	tone_numbers = ["0","1","2","3","4"]

	ignorable_characters_with_tone_numbers = []
	ignorable_characters_with_tone_numbers.extend(ignorable_characters)
	ignorable_characters_with_tone_numbers.extend(tone_numbers)

	# list which will contain the pinyin syllables
	pinyin_syllables = []
	text_components = {}
	syllables_with_ignorable_characters_counter = 0

	def __init__(self):
		self.text = None

	def isPartOfAPinyinSyllable(self, partial_syllable):
		result = False
		for i in range(0, len(self.possible_pinyin_syllables)):
			if partial_syllable.lower() in self.possible_pinyin_syllables[i]:
				result = True
		return result

	def isCompletePinyinSyllable(self, text):
		return text.lower() in self.possible_pinyin_syllables

	def isPinyinSyllable(self, text):
		return self.isCompletePinyinSyllable(self.stripToneNumber(text))

	def parse(self):
		self.pinyin_syllables = []
		self.text_components = {}
		self.syllables_with_ignorable_characters_counter = 0
		
		longest_matching_syllable_found = ""
		longest_syllable_length = 0

		# in case the text starts with ignorable characters
		self.text = self.removeIgnorableCharactersAndToneNumbers(self.text)

		while len(self.text) > 0: # while there are still characters in the text
			for syllable in self.possible_pinyin_syllables: # for each syllable in the list of possible pinyin syllables
				if self.text.lower().find(syllable) == 0: # if the syllable is found at the beginning of the string
					if len(syllable) > longest_syllable_length:
						longest_syllable_length = len(syllable)
						longest_matching_syllable_found = self.text[0:len(syllable)] # append the syllable of the text to preserve capital letters (syllables in the list of possible syllables are lower case syllables)

			# if there is still something in the text but no syllable fits the text is invalid
			if (len(self.text) > 0) and (longest_matching_syllable_found == "") and (longest_syllable_length == 0):
				raise PinyinParseException(
					"Invalid pinyin input: \n" +
					"Remaining text:|"+self.text+"|\n" +
					"Longest syllable length:|"+str(longest_syllable_length)+"|\n" +
					"Longest syllable fitting:|"+longest_matching_syllable_found+"|"
				)
			else:
				self.text = self.text[longest_syllable_length:]

				if len(self.text) > 0: # is there is still text
					if self.text[0] in self.tone_numbers: # if there is a leading tone number
						longest_matching_syllable_found = longest_matching_syllable_found + self.text[0] # add that tone number to the current syllable
						self.text = self.text[1:] # remove the tone number from the text

				# save it as a syllable
				self.pinyin_syllables.append(longest_matching_syllable_found)
				# save it in the dictionary
				self.addToTextComponents(longest_matching_syllable_found)
				# update remaining text
				self.text = self.removeIgnorableCharactersAndToneNumbers(self.text)

				# reset values
				longest_syllable_length = 0
				longest_matching_syllable_found = ""

	def addToTextComponents(self, value):
		self.text_components[self.syllables_with_ignorable_characters_counter] = value
		self.syllables_with_ignorable_characters_counter += 1

	def removeIgnorableCharacters(self, text):
		while (len(text) > 0) and (text[0] in self.ignorable_characters):
			self.addToTextComponents(text[0])
			#print("Removing ignorable character:" + self.text[0])
			text = text[1:]
		return text

	def removeIgnorableCharactersAndToneNumbers(self, text):
		while (len(text) > 0) and (text[0] in self.ignorable_characters_with_tone_numbers):
			self.addToTextComponents(text[0])
			#print("Removing ignorable character:" + self.text[0])
			text = text[1:]
		return text

	@staticmethod
	def stripToneNumber(syllable):
		syllable = str(syllable)
		#print(type(syllable))

		if syllable[-1] in ['0','1','2','3','4']:
			return syllable[:-1]
		return syllable

	"""
	GETTER
	"""

	def getSyllables(self):
		return self.pinyin_syllables

	def getTextComponents(self):
		return self.text_components

	def getCompletePinyinText(self):
		pass

	"""
	SETTER
	"""
	def setText(self, value):
		self.text = value