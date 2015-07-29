__author__ = 'Xiaolong'

from unittest import TestCase
from pinyintransformer.PinyinTones2NumbersTransformer import PinyinTones2NumbersTransformer


class TestPinyinTones2NumbersTransformer(TestCase):
	
	def setUp (self):
		self.pinyin_tones_2_numbers_transformer = PinyinTones2NumbersTransformer()
	
	def test_transform (self):
		toned_text = "Míngtiānnǐděiqǐchuānghěnzǎo. Wǎnān!"
		numbered_text = "Ming2tian1ni3dei3qi3chuang1hen3zao3. Wan3an1!"
		self.assertEquals(self.pinyin_tones_2_numbers_transformer.transform(toned_text), numbered_text)
		
		toned_text = "Míngtiān(nǐděiqǐchuānghěnzǎo. Wǎnān!"
		numbered_text = "Ming2tian1(ni3dei3qi3chuang1hen3zao3. Wan3an1!"
		self.assertEquals(self.pinyin_tones_2_numbers_transformer.transform(toned_text), numbered_text)
		
		toned_text = "Míngtiān(nǐděiqǐchuāng]hěnzǎo. Wǎnān!"
		numbered_text = "Ming2tian1(ni3dei3qi3chuang1]hen3zao3. Wan3an1!"
		self.assertEquals(self.pinyin_tones_2_numbers_transformer.transform(toned_text), numbered_text)
		
		toned_text = "Míngtiānnǐ!děi?qǐ chuānghěnzǎo. Wǎnān!"
		numbered_text = "Ming2tian1ni3!dei3?qi3 chuang1hen3zao3. Wan3an1!"
		self.assertEquals(self.pinyin_tones_2_numbers_transformer.transform(toned_text), numbered_text)
		
		toned_text = "yóuxiāngdìzhǐ"
		numbered_text = "you2xiang1di4zhi3"
		self.assertEquals(self.pinyin_tones_2_numbers_transformer.transform(toned_text), numbered_text)
		
	def test_getToneNumberOfTonedSyllable (self):
		self.assertEquals(self.pinyin_tones_2_numbers_transformer.getToneNumberOfTonedSyllable("ne"), 0)
		self.assertEquals(self.pinyin_tones_2_numbers_transformer.getToneNumberOfTonedSyllable("a"), 0)
		self.assertEquals(self.pinyin_tones_2_numbers_transformer.getToneNumberOfTonedSyllable("ān"), 1)
		self.assertEquals(self.pinyin_tones_2_numbers_transformer.getToneNumberOfTonedSyllable("péng"), 2)
		self.assertEquals(self.pinyin_tones_2_numbers_transformer.getToneNumberOfTonedSyllable("nǐ"), 3)
		self.assertEquals(self.pinyin_tones_2_numbers_transformer.getToneNumberOfTonedSyllable("jiào"), 4)
	
	def test_getFirstIndexOfTonedVocal (self):
		self.assertEquals(self.pinyin_tones_2_numbers_transformer.getFirstIndexOfTonedVocal("Zǎoshànghǎo!"), 1)
		self.assertEquals(self.pinyin_tones_2_numbers_transformer.getFirstIndexOfTonedVocal("Ān!"), 0)
		self.assertEquals(self.pinyin_tones_2_numbers_transformer.getFirstIndexOfTonedVocal("ān!"), 0)
		self.assertEquals(self.pinyin_tones_2_numbers_transformer.getFirstIndexOfTonedVocal("An!"), -1)
		self.assertEquals(self.pinyin_tones_2_numbers_transformer.getFirstIndexOfTonedVocal("Zhōngguó!"), 2)
		self.assertEquals(self.pinyin_tones_2_numbers_transformer.getFirstIndexOfTonedVocal("Zhongguó!"), 7)
		self.assertEquals(self.pinyin_tones_2_numbers_transformer.getFirstIndexOfTonedVocal("Zaoshanghao!"), -1)
		
	def test_getPositionsOfTonedVocals (self):
		self.assertEquals(self.pinyin_tones_2_numbers_transformer.getPositionsOfTonedVocals("Zǎoshànghǎo!"), [(1, 3), (5, 4), (9, 3)])
		self.assertEquals(self.pinyin_tones_2_numbers_transformer.getPositionsOfTonedVocals("Wǒyàoqùzhōngguó!!"), [(1, 3), (3, 4), (6, 4), (9, 1), (14, 2)])
	
	def test_getToneNumberOfTonedVocal (self):
		for vocal in ['a', 'e', 'i', 'o', 'u', 'ü', 'A', 'E', 'I', 'O', 'U', 'Ü']:
			self.assertEquals(self.pinyin_tones_2_numbers_transformer.getToneNumberOfTonedVocal(vocal), 0)
		
		for tonedVocal in ['ā', 'ē', 'ī', 'ō', 'ū', 'ǖ', 'Ā', 'Ē', 'Ī', 'Ō', 'Ū', 'Ǖ']:
			self.assertEquals(self.pinyin_tones_2_numbers_transformer.getToneNumberOfTonedVocal(tonedVocal), 1)
	
		for tonedVocal in ['á', 'é', 'í', 'ó', 'ú', 'ǘ', 'Á', 'É', 'Í', 'Ó', 'Ú', 'Ǘ']:
			self.assertEquals(self.pinyin_tones_2_numbers_transformer.getToneNumberOfTonedVocal(tonedVocal), 2)
			
		for tonedVocal in ['ǎ', 'ě', 'ǐ', 'ǒ', 'ǔ', 'ǚ', 'Ǎ', 'Ě', 'Ǐ', 'Ǒ', 'Ǔ', 'Ǚ']:
			self.assertEquals(self.pinyin_tones_2_numbers_transformer.getToneNumberOfTonedVocal(tonedVocal), 3)
		
		for tonedVocal in ['à', 'è', 'ì', 'ò', 'ù', 'ǜ', 'À', 'È', 'Ì', 'Ò', 'Ù', 'Ǜ']:
			self.assertEquals(self.pinyin_tones_2_numbers_transformer.getToneNumberOfTonedVocal(tonedVocal), 4)
		
	
	def test_getVocalOfTonedVocal (self):
		for tonedVocal in ['ā', 'á', 'ǎ', 'à']:
			self.assertEquals(self.pinyin_tones_2_numbers_transformer.getVocalOfTonedVocal(tonedVocal), 'a')
		for tonedVocal in ['ē', 'é', 'ě', 'è']:
			self.assertEquals(self.pinyin_tones_2_numbers_transformer.getVocalOfTonedVocal(tonedVocal), 'e')
		for tonedVocal in ['ī', 'í', 'ǐ', 'ì']:
			self.assertEquals(self.pinyin_tones_2_numbers_transformer.getVocalOfTonedVocal(tonedVocal), 'i')
		for tonedVocal in ['ō', 'ó', 'ǒ', 'ò']:
			self.assertEquals(self.pinyin_tones_2_numbers_transformer.getVocalOfTonedVocal(tonedVocal), 'o')
		for tonedVocal in ['ū', 'ú', 'ǔ', 'ù']:
			self.assertEquals(self.pinyin_tones_2_numbers_transformer.getVocalOfTonedVocal(tonedVocal), 'u')
		for tonedVocal in ['ǖ', 'ǘ', 'ǚ', 'ǜ']:
			self.assertEquals(self.pinyin_tones_2_numbers_transformer.getVocalOfTonedVocal(tonedVocal), 'ü')
		
		for tonedVocal in ['Ā', 'Á', 'Ǎ', 'À']:
			self.assertEquals(self.pinyin_tones_2_numbers_transformer.getVocalOfTonedVocal(tonedVocal), 'A')
		for tonedVocal in ['Ē', 'É', 'Ě', 'È']:
			self.assertEquals(self.pinyin_tones_2_numbers_transformer.getVocalOfTonedVocal(tonedVocal), 'E')
		for tonedVocal in ['Ī', 'Í', 'Ǐ', 'Ì']:
			self.assertEquals(self.pinyin_tones_2_numbers_transformer.getVocalOfTonedVocal(tonedVocal), 'I')
		for tonedVocal in ['Ō', 'Ó', 'Ǒ', 'Ò']:
			self.assertEquals(self.pinyin_tones_2_numbers_transformer.getVocalOfTonedVocal(tonedVocal), 'O')
		for tonedVocal in ['Ū', 'Ú', 'Ǔ', 'Ù']:
			self.assertEquals(self.pinyin_tones_2_numbers_transformer.getVocalOfTonedVocal(tonedVocal), 'U')
		for tonedVocal in ['Ǖ', 'Ǘ', 'Ǚ', 'Ǜ']:
			self.assertEquals(self.pinyin_tones_2_numbers_transformer.getVocalOfTonedVocal(tonedVocal), 'Ü')
	
	def test_getUntonedText (self):
		self.assertEquals(self.pinyin_tones_2_numbers_transformer.getUntonedText("Zǎoshànghǎo!", [(1, 3), (5, 4), (9, 3)]), "Zaoshanghao!")
		self.assertEquals(self.pinyin_tones_2_numbers_transformer.getUntonedText("Wǎnshànghǎo!", [(1, 3), (5, 4), (9, 3)]), "Wanshanghao!")
		self.assertEquals(self.pinyin_tones_2_numbers_transformer.getUntonedText("Zǎo shàng hǎo!", [(1, 3), (6, 4), (11, 3)]), "Zao shang hao!")
		self.assertEquals(self.pinyin_tones_2_numbers_transformer.getUntonedText("Wǎn shàng hǎo!", [(1, 3), (6, 4), (11, 3)]), "Wan shang hao!")
		self.assertEquals(self.pinyin_tones_2_numbers_transformer.getUntonedText("Wǎn] (shàng '!hǎo!", [(1, 3), (8, 4), (15, 3)]), "Wan] (shang '!hao!")
	
	def test_mergeTextComponentsAndToneNumbers (self):
		self.assertEquals(
			self.pinyin_tones_2_numbers_transformer.mergeTextComponentsAndToneNumbers(
				["Zao", "shang", "hao", "!"], [(1, 3), (5, 4), (9, 3)]
			),
			"Zao3shang4hao3!"
		)
		# self.assertEquals(True, True)
	
	def test_getIndexOfTextPositionInTextComponents (self):
		self.assertEquals(self.pinyin_tones_2_numbers_transformer.getIndexOfTextPositionInTextComponents(1, ["Zao", "shang", "hao", "!"]), 0)
		self.assertEquals(self.pinyin_tones_2_numbers_transformer.getIndexOfTextPositionInTextComponents(5, ["Zao", "shang", "hao", "!"]), 1)
		self.assertEquals(self.pinyin_tones_2_numbers_transformer.getIndexOfTextPositionInTextComponents(9, ["Zao", "shang", "hao", "!"]), 2)
		
		self.assertEquals(self.pinyin_tones_2_numbers_transformer.getIndexOfTextPositionInTextComponents(3, ["Ma", "ma"]), 1)
		self.assertEquals(self.pinyin_tones_2_numbers_transformer.getIndexOfTextPositionInTextComponents(0, ["An"]), 0)
		self.assertEquals(self.pinyin_tones_2_numbers_transformer.getIndexOfTextPositionInTextComponents(0, ["an"]), 0)
		self.assertEquals(self.pinyin_tones_2_numbers_transformer.getIndexOfTextPositionInTextComponents(1, ["An"]), 0)
		self.assertEquals(self.pinyin_tones_2_numbers_transformer.getIndexOfTextPositionInTextComponents(1, ["an"]), 0)