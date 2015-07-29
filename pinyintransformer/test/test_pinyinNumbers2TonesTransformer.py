from unittest import TestCase
from pinyintransformer.PinyinNumbers2TonesTransformer import PinyinNumbers2TonesTransformer

__author__ = 'Xiaolong'


class TestPinyinNumbers2TonesTransformer(TestCase):
	
	def setUp (self):
		self.pinyin_numbers_2_tones_transformer = PinyinNumbers2TonesTransformer()
	
	def test_transform (self):
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.transform("ni3jin1tian1hai2you3ke4ma"), "nǐjīntiānháiyǒukèma")
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.transform("ni3 jin1tian1 hai2 you3 ke4 ma"), "nǐ jīntiān hái yǒu kè ma")
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.transform("Ni3 jin1tian1 hai2 you3 ke4 ma"), "Nǐ jīntiān hái yǒu kè ma")
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.transform("Ni3 jin1tian1 hai2 you3 ke4 ma?"), "Nǐ jīntiān hái yǒu kè ma?")
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.transform("Ni3 jin1tian1 hai2 you3 ke4 ma? (Wo3 mei2you3.)"), "Nǐ jīntiān hái yǒu kè ma? (Wǒ méiyǒu.)")
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.transform("Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 mei2you3.)"), "Nǐ jīn!\"\'\n\t{[(tiān hái yǒu kè ma? (Wǒ méiyǒu.)")
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.transform("[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 mei2you3.)"), "[Nǐ jīn!\"\'\n\t{[(tiān hái yǒu kè ma? (Wǒ méiyǒu.)")
	
	def test_getToneNumberOfSyllable (self):
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getToneNumberOfSyllable("ma"), 0)
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getToneNumberOfSyllable("ma1"), 1)
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getToneNumberOfSyllable("ming2"), 2)
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getToneNumberOfSyllable("ni3"), 3)
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getToneNumberOfSyllable("jiao4"), 4)
		
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getToneNumberOfSyllable("Ma"), 0)
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getToneNumberOfSyllable("Ma1"), 1)
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getToneNumberOfSyllable("Ming2"), 2)
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getToneNumberOfSyllable("Ni3"), 3)
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getToneNumberOfSyllable("Jiao4"), 4)
		
		
	def test_getTonedVocals (self):
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedVocals(['a', 'a', 'a', 'a', 'a'], [0, 1, 2, 3, 4]), ['a', 'ā', 'á', 'ǎ', 'à'])
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedVocals(['A', 'A', 'A', 'A', 'A'], [0, 1, 2, 3, 4]), ['A', 'Ā', 'Á', 'Ǎ', 'À'])
		
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedVocals(['e', 'e', 'e', 'e', 'e'], [0, 1, 2, 3, 4]), ['e', 'ē', 'é', 'ě', 'è'])
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedVocals(['E', 'E', 'E', 'E', 'E'], [0, 1, 2, 3, 4]), ['E', 'Ē', 'É', 'Ě', 'È'])
		
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedVocals(['i', 'i', 'i', 'i', 'i'], [0, 1, 2, 3, 4]), ['i', 'ī', 'í', 'ǐ', 'ì'])
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedVocals(['I', 'I', 'I', 'I', 'I'], [0, 1, 2, 3, 4]), ['I', 'Ī', 'Í', 'Ǐ', 'Ì'])
		
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedVocals(['o', 'o', 'o', 'o', 'o'], [0, 1, 2, 3, 4]), ['o', 'ō', 'ó', 'ǒ', 'ò'])
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedVocals(['O', 'O', 'O', 'O', 'O'], [0, 1, 2, 3, 4]), ['O', 'Ō', 'Ó', 'Ǒ', 'Ò'])
		
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedVocals(['u', 'u', 'u', 'u', 'u'], [0, 1, 2, 3, 4]), ['u', 'ū', 'ú', 'ǔ', 'ù'])
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedVocals(['U', 'U', 'U', 'U', 'U'], [0, 1, 2, 3, 4]), ['U', 'Ū', 'Ú', 'Ǔ', 'Ù'])
		
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedVocals(['ü', 'ü', 'ü', 'ü', 'ü'], [0, 1, 2, 3, 4]), ['ü', 'ǖ', 'ǘ', 'ǚ', 'ǜ'])
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedVocals(['Ü', 'Ü', 'Ü', 'Ü', 'Ü'], [0, 1, 2, 3, 4]), ['Ü', 'Ǖ', 'Ǘ', 'Ǚ', 'Ǜ'])
		
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedVocals(['a', 'e', 'i', 'o', 'u', 'ü'], [0, 1, 2, 3, 4, 1]), ['a', 'ē', 'í', 'ǒ', 'ù', 'ǖ'])
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedVocals(['A', 'E', 'I', 'O', 'U', 'Ü'], [0, 1, 2, 3, 4, 1]), ['A', 'Ē', 'Í', 'Ǒ', 'Ù', 'Ǖ'])
	
	def test_getTonedVocalFromVocalAndToneNumber (self):
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedVocalFromVocalAndToneNumber("a", 0), "a")
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedVocalFromVocalAndToneNumber("a", 1), "ā")
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedVocalFromVocalAndToneNumber("a", 2), "á")
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedVocalFromVocalAndToneNumber("a", 3), "ǎ")
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedVocalFromVocalAndToneNumber("a", 4), "à")
		
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedVocalFromVocalAndToneNumber("A", 0), "A")
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedVocalFromVocalAndToneNumber("A", 1), "Ā")
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedVocalFromVocalAndToneNumber("A", 2), "Á")
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedVocalFromVocalAndToneNumber("A", 3), "Ǎ")
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedVocalFromVocalAndToneNumber("A", 4), "À")
		
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedVocalFromVocalAndToneNumber("e", 0), "e")
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedVocalFromVocalAndToneNumber("e", 1), "ē")
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedVocalFromVocalAndToneNumber("e", 2), "é")
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedVocalFromVocalAndToneNumber("e", 3), "ě")
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedVocalFromVocalAndToneNumber("e", 4), "è")
		
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedVocalFromVocalAndToneNumber("E", 0), "E")
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedVocalFromVocalAndToneNumber("E", 1), "Ē")
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedVocalFromVocalAndToneNumber("E", 2), "É")
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedVocalFromVocalAndToneNumber("E", 3), "Ě")
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedVocalFromVocalAndToneNumber("E", 4), "È")
		
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedVocalFromVocalAndToneNumber("i", 0), "i")
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedVocalFromVocalAndToneNumber("i", 1), "ī")
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedVocalFromVocalAndToneNumber("i", 2), "í")
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedVocalFromVocalAndToneNumber("i", 3), "ǐ")
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedVocalFromVocalAndToneNumber("i", 4), "ì")
		
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedVocalFromVocalAndToneNumber("I", 0), "I")
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedVocalFromVocalAndToneNumber("I", 1), "Ī")
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedVocalFromVocalAndToneNumber("I", 2), "Í")
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedVocalFromVocalAndToneNumber("I", 3), "Ǐ")
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedVocalFromVocalAndToneNumber("I", 4), "Ì")
		
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedVocalFromVocalAndToneNumber("o", 0), "o")
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedVocalFromVocalAndToneNumber("o", 1), "ō")
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedVocalFromVocalAndToneNumber("o", 2), "ó")
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedVocalFromVocalAndToneNumber("o", 3), "ǒ")
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedVocalFromVocalAndToneNumber("o", 4), "ò")
		
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedVocalFromVocalAndToneNumber("O", 0), "O")
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedVocalFromVocalAndToneNumber("O", 1), "Ō")
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedVocalFromVocalAndToneNumber("O", 2), "Ó")
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedVocalFromVocalAndToneNumber("O", 3), "Ǒ")
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedVocalFromVocalAndToneNumber("O", 4), "Ò")
		
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedVocalFromVocalAndToneNumber("u", 0), "u")
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedVocalFromVocalAndToneNumber("u", 1), "ū")
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedVocalFromVocalAndToneNumber("u", 2), "ú")
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedVocalFromVocalAndToneNumber("u", 3), "ǔ")
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedVocalFromVocalAndToneNumber("u", 4), "ù")
		
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedVocalFromVocalAndToneNumber("U", 0), "U")
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedVocalFromVocalAndToneNumber("U", 1), "Ū")
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedVocalFromVocalAndToneNumber("U", 2), "Ú")
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedVocalFromVocalAndToneNumber("U", 3), "Ǔ")
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedVocalFromVocalAndToneNumber("U", 4), "Ù")
		
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedVocalFromVocalAndToneNumber("ü", 0), "ü")
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedVocalFromVocalAndToneNumber("ü", 1), "ǖ")
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedVocalFromVocalAndToneNumber("ü", 2), "ǘ")
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedVocalFromVocalAndToneNumber("ü", 3), "ǚ")
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedVocalFromVocalAndToneNumber("ü", 4), "ǜ")
		
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedVocalFromVocalAndToneNumber("Ü", 0), "Ü")
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedVocalFromVocalAndToneNumber("Ü", 1), "Ǖ")
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedVocalFromVocalAndToneNumber("Ü", 2), "Ǘ")
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedVocalFromVocalAndToneNumber("Ü", 3), "Ǚ")
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedVocalFromVocalAndToneNumber("Ü", 4), "Ǜ")
		
	def test_getTonedSyllables (self):
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedSyllables(["Ni3", "hao3", "ma"]), ["Nǐ", "hǎo", "ma"])
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedSyllables(["Ni3", "xiang3", "qu4", "zhong1", "guo2", "ma"]), ["Nǐ","xiǎng","qù","zhōng","guó","ma"])
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedSyllables(["Ni3", "jiao4", "shen2", "me", "ming2", "zi"]), ["Nǐ","jiào","shén","me","míng","zi"])
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedSyllables(["Xian1", "zai4", "ji3", "dian3", "le"]), ["Xiān", "zài", "jǐ", "diǎn", "le"])
	
	def test_getTonedSyllableFromSyllableAndToneNumber (self):
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedSyllableFromSyllableAndToneNumber("Ni", 3), "Nǐ")
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedSyllableFromSyllableAndToneNumber("hao", 3), "hǎo")
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedSyllableFromSyllableAndToneNumber("ma", 0), "ma")
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedSyllableFromSyllableAndToneNumber("Zhe", 4), "Zhè")
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedSyllableFromSyllableAndToneNumber("shi", 4), "shì")
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedSyllableFromSyllableAndToneNumber("yi", 1), "yī")
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedSyllableFromSyllableAndToneNumber("wei", 4), "wèi")
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedSyllableFromSyllableAndToneNumber("jiao", 4), "jiào")
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedSyllableFromSyllableAndToneNumber("shou", 4), "shòu")
	
	def test_getTonedSyllableFromNumberedSyllable (self):
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedSyllableFromNumberedSyllable("Ni3"), "Nǐ")
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedSyllableFromNumberedSyllable("hao3"), "hǎo")
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedSyllableFromNumberedSyllable("ma"), "ma")
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedSyllableFromNumberedSyllable("Zhe4"), "Zhè")
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedSyllableFromNumberedSyllable("shi4"), "shì")
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedSyllableFromNumberedSyllable("yi1"), "yī")
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedSyllableFromNumberedSyllable("wei4"), "wèi")
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedSyllableFromNumberedSyllable("jiao4"), "jiào")
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getTonedSyllableFromNumberedSyllable("shou4"), "shòu")
	
	def test_getLastVocalFromText (self):
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getLastVocal("Ni3hao3ma?"), "a")
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getLastVocal("Ni3xiang3qu4zhong1guo2ma?"), "a")
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getLastVocal("Ni3jiao4shen2meming2zi?"), "i")
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.getLastVocal("Xian1zai4ji3dian3le?"), "e")
	
	def test_removeToneNumber (self):
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.removeToneNumbersFromText("Ni3"), "Ni")
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.removeToneNumbersFromText("An1"), "An")
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.removeToneNumbersFromText("Wan3"), "Wan")
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.removeToneNumbersFromText("Zhong1"), "Zhong")
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.removeToneNumbersFromText("Zhong1 "), "Zhong ")
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.removeToneNumbersFromText("zhong1"), "zhong")
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.removeToneNumbersFromText("zhong1 "), "zhong ")
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.removeToneNumbersFromText(""), "")
		self.assertEquals(self.pinyin_numbers_2_tones_transformer.removeToneNumbersFromText("Ni3hao3ma?"), "Nihaoma?")
	
	def test_isPinyinSyllable (self):
		self.assertTrue(self.pinyin_numbers_2_tones_transformer.isPinyinSyllable("Ni3"))
		self.assertTrue(self.pinyin_numbers_2_tones_transformer.isPinyinSyllable("hao3"))
		self.assertTrue(self.pinyin_numbers_2_tones_transformer.isPinyinSyllable("ma"))
		self.assertTrue(self.pinyin_numbers_2_tones_transformer.isPinyinSyllable("Zhong1"))
		self.assertTrue(self.pinyin_numbers_2_tones_transformer.isPinyinSyllable("guo2"))
		self.assertTrue(self.pinyin_numbers_2_tones_transformer.isPinyinSyllable("shou1"))
		self.assertTrue(self.pinyin_numbers_2_tones_transformer.isPinyinSyllable("shu1"))
		self.assertTrue(self.pinyin_numbers_2_tones_transformer.isPinyinSyllable("jiao4"))
		self.assertFalse(self.pinyin_numbers_2_tones_transformer.isPinyinSyllable("Zhon"))
		self.assertFalse(self.pinyin_numbers_2_tones_transformer.isPinyinSyllable("zhon"))
		self.assertFalse(self.pinyin_numbers_2_tones_transformer.isPinyinSyllable("sho3"))
		self.assertFalse(self.pinyin_numbers_2_tones_transformer.isPinyinSyllable("shou3 "))