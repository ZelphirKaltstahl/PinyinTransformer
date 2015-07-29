from unittest import TestCase
from pinyintransformer.parser.PinyinParserMixed import PinyinParserMixed

__author__ = 'xiaolong'


class TestPinyinParserMixed(TestCase):
	
	def setUp(self):
		self.pinyin_parser_mixed = PinyinParserMixed()
	
	def test_parse (self):
		self.assertEquals(self.pinyin_parser_mixed.parse("ni3jin1tian1hai2you3ke4ma"), ["ni3", "jin1", "tian1", "hai2", "you3", "ke4", "ma"])
		self.assertEquals(self.pinyin_parser_mixed.parse("nǐjīntiānháiyǒukèma"), ["nǐ", "jīn", "tiān", "hái", "yǒu", "kè", "ma"])
		self.assertEquals(self.pinyin_parser_mixed.parse("nǐjin1tian1háiyǒukèma"), ["nǐ", "jin1", "tian1", "hái", "yǒu", "kè", "ma"])
		
		self.assertEquals(self.pinyin_parser_mixed.parse("ni3 jin1tian1 hai2 you3 ke4 ma"), ["ni3", " ", "jin1", "tian1", " ", "hai2", " ", "you3", " ", "ke4", " ", "ma"])
		self.assertEquals(self.pinyin_parser_mixed.parse("nǐ jīntiān hái yǒu kè ma"), ["nǐ", " ", "jīn", "tiān", " ", "hái", " ", "yǒu", " ", "kè", " ", "ma"])
		self.assertEquals(self.pinyin_parser_mixed.parse("ni3 jin1tian1 hái you3 ke4 ma"), ["ni3", " ", "jin1", "tian1", " ", "hái", " ", "you3", " ", "ke4", " ", "ma"])
		
		self.assertEquals(self.pinyin_parser_mixed.parse("Ni3 jin1tian1 hai2 you3 ke4 ma"), ["Ni3", " ", "jin1", "tian1", " ", "hai2", " ", "you3", " ", "ke4", " ", "ma"])
		self.assertEquals(self.pinyin_parser_mixed.parse("Nǐ jīntiān hái yǒu kè ma"), ["Nǐ", " ", "jīn", "tiān", " ", "hái", " ", "yǒu", " ", "kè", " ", "ma"])
		self.assertEquals(self.pinyin_parser_mixed.parse("Ni3 jin1tian1 hai2 you3 kè ma0"), ["Ni3", " ", "jin1", "tian1", " ", "hai2", " ", "you3", " ", "kè", " ", "ma0"])
		
		self.assertEquals(self.pinyin_parser_mixed.parse("Ni3 jin1tian1 hai2 you3 ke4 ma?"), ["Ni3"," ","jin1","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"])
		self.assertEquals(self.pinyin_parser_mixed.parse("Nǐ jīntiān hái yǒu kè ma?"), ["Nǐ"," ","jīn","tiān"," ","hái"," ","yǒu"," ","kè"," ","ma","?"])
		self.assertEquals(self.pinyin_parser_mixed.parse("Ni3 jīntiān hai2 you3 ke4 ma?"), ["Ni3"," ","jīn","tiān"," ","hai2"," ","you3"," ","ke4"," ","ma","?"])
		
		self.assertEquals(self.pinyin_parser_mixed.parse("Ni3 jin1tian1 hai2 you3 ke4 ma? (Wo3 mei2you3.)"), ["Ni3"," ","jin1","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","mei2","you3",".",")"])
		self.assertEquals(self.pinyin_parser_mixed.parse("Nǐ jīntiān hái yǒu kè ma? (Wǒ méiyǒu.)"), ["Nǐ"," ","jīn","tiān"," ","hái"," ","yǒu"," ","kè"," ","ma","?"," ","(","Wǒ"," ","méi","yǒu",".",")"])
		self.assertEquals(self.pinyin_parser_mixed.parse("Ni3 jin1tian1 hai2 you3 ke4 ma? (Wǒ méiyǒu.)"), ["Ni3"," ","jin1","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wǒ"," ","méi","yǒu",".",")"])
		
		self.assertEquals(self.pinyin_parser_mixed.parse("Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 mei2you3.)"), ["Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","mei2","you3",".",")"])
		self.assertEquals(self.pinyin_parser_mixed.parse("Nǐ jīn!\"\'\n\t{[(tiān hái yǒu kè ma? (Wǒ méiyǒu.)"), ["Nǐ"," ","jīn","!","\"","\'","\n","\t","{","[","(","tiān"," ","hái"," ","yǒu"," ","kè"," ","ma","?"," ","(","Wǒ"," ","méi","yǒu",".",")"])
		self.assertEquals(self.pinyin_parser_mixed.parse("Nǐ jīn!\"\'\n\t{[(tian1 hái yǒu kè ma? (Wǒ méiyǒu.)"), ["Nǐ"," ","jīn","!","\"","\'","\n","\t","{","[","(","tian1"," ","hái"," ","yǒu"," ","kè"," ","ma","?"," ","(","Wǒ"," ","méi","yǒu",".",")"])
		
		self.assertEquals(self.pinyin_parser_mixed.parse("[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 mei2you3.)"), ["[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","mei2","you3",".",")"])
		self.assertEquals(self.pinyin_parser_mixed.parse("[Nǐ jīn!\"\'\n\t{[(tiān hái yǒu kè ma? (Wǒ méiyǒu.)"), ["[","Nǐ"," ","jīn","!","\"","\'","\n","\t","{","[","(","tiān"," ","hái"," ","yǒu"," ","kè"," ","ma","?"," ","(","Wǒ"," ","méi","yǒu",".",")"])
		self.assertEquals(self.pinyin_parser_mixed.parse("[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)"), ["[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")"])
	
	def test_fastParse(self):
		self.assertEquals(self.pinyin_parser_mixed.fastParse("ni3jin1tian1hai2you3ke4ma"), ["ni3", "jin1", "tian1", "hai2", "you3", "ke4", "ma"])
		self.assertEquals(self.pinyin_parser_mixed.fastParse("nǐjīntiānháiyǒukèma"), ["nǐ", "jīn", "tiān", "hái", "yǒu", "kè", "ma"])
		self.assertEquals(self.pinyin_parser_mixed.fastParse("nǐjin1tian1háiyǒukèma"), ["nǐ", "jin1", "tian1", "hái", "yǒu", "kè", "ma"])
		
		self.assertEquals(self.pinyin_parser_mixed.fastParse("ni3 jin1tian1 hai2 you3 ke4 ma"), ["ni3", " ", "jin1", "tian1", " ", "hai2", " ", "you3", " ", "ke4", " ", "ma"])
		self.assertEquals(self.pinyin_parser_mixed.fastParse("nǐ jīntiān hái yǒu kè ma"), ["nǐ", " ", "jīn", "tiān", " ", "hái", " ", "yǒu", " ", "kè", " ", "ma"])
		self.assertEquals(self.pinyin_parser_mixed.fastParse("ni3 jin1tian1 hái you3 ke4 ma"), ["ni3", " ", "jin1", "tian1", " ", "hái", " ", "you3", " ", "ke4", " ", "ma"])
		
		self.assertEquals(self.pinyin_parser_mixed.fastParse("Ni3 jin1tian1 hai2 you3 ke4 ma"), ["Ni3", " ", "jin1", "tian1", " ", "hai2", " ", "you3", " ", "ke4", " ", "ma"])
		self.assertEquals(self.pinyin_parser_mixed.fastParse("Nǐ jīntiān hái yǒu kè ma"), ["Nǐ", " ", "jīn", "tiān", " ", "hái", " ", "yǒu", " ", "kè", " ", "ma"])
		self.assertEquals(self.pinyin_parser_mixed.fastParse("Ni3 jin1tian1 hai2 you3 kè ma0"), ["Ni3", " ", "jin1", "tian1", " ", "hai2", " ", "you3", " ", "kè", " ", "ma0"])
		
		self.assertEquals(self.pinyin_parser_mixed.fastParse("Ni3 jin1tian1 hai2 you3 ke4 ma?"), ["Ni3"," ","jin1","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"])
		self.assertEquals(self.pinyin_parser_mixed.fastParse("Nǐ jīntiān hái yǒu kè ma?"), ["Nǐ"," ","jīn","tiān"," ","hái"," ","yǒu"," ","kè"," ","ma","?"])
		self.assertEquals(self.pinyin_parser_mixed.fastParse("Ni3 jīntiān hai2 you3 ke4 ma?"), ["Ni3"," ","jīn","tiān"," ","hai2"," ","you3"," ","ke4"," ","ma","?"])
		
		self.assertEquals(self.pinyin_parser_mixed.fastParse("Ni3 jin1tian1 hai2 you3 ke4 ma? (Wo3 mei2you3.)"), ["Ni3"," ","jin1","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","mei2","you3",".",")"])
		self.assertEquals(self.pinyin_parser_mixed.fastParse("Nǐ jīntiān hái yǒu kè ma? (Wǒ méiyǒu.)"), ["Nǐ"," ","jīn","tiān"," ","hái"," ","yǒu"," ","kè"," ","ma","?"," ","(","Wǒ"," ","méi","yǒu",".",")"])
		self.assertEquals(self.pinyin_parser_mixed.fastParse("Ni3 jin1tian1 hai2 you3 ke4 ma? (Wǒ méiyǒu.)"), ["Ni3"," ","jin1","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wǒ"," ","méi","yǒu",".",")"])
		
		self.assertEquals(self.pinyin_parser_mixed.fastParse("Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 mei2you3.)"), ["Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","mei2","you3",".",")"])
		self.assertEquals(self.pinyin_parser_mixed.fastParse("Nǐ jīn!\"\'\n\t{[(tiān hái yǒu kè ma? (Wǒ méiyǒu.)"), ["Nǐ"," ","jīn","!","\"","\'","\n","\t","{","[","(","tiān"," ","hái"," ","yǒu"," ","kè"," ","ma","?"," ","(","Wǒ"," ","méi","yǒu",".",")"])
		self.assertEquals(self.pinyin_parser_mixed.fastParse("Nǐ jīn!\"\'\n\t{[(tian1 hái yǒu kè ma? (Wǒ méiyǒu.)"), ["Nǐ"," ","jīn","!","\"","\'","\n","\t","{","[","(","tian1"," ","hái"," ","yǒu"," ","kè"," ","ma","?"," ","(","Wǒ"," ","méi","yǒu",".",")"])
		
		self.assertEquals(self.pinyin_parser_mixed.fastParse("[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 mei2you3.)"), ["[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","mei2","you3",".",")"])
		self.assertEquals(self.pinyin_parser_mixed.fastParse("[Nǐ jīn!\"\'\n\t{[(tiān hái yǒu kè ma? (Wǒ méiyǒu.)"), ["[","Nǐ"," ","jīn","!","\"","\'","\n","\t","{","[","(","tiān"," ","hái"," ","yǒu"," ","kè"," ","ma","?"," ","(","Wǒ"," ","méi","yǒu",".",")"])
		self.assertEquals(self.pinyin_parser_mixed.fastParse("[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)"), ["[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")"])
		
		long_string = "[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)[Ni3 jin1!\"\'\n\t{[(tian1 hai2 you3 ke4 ma? (Wo3 méiyǒu.)"
		long_text_components = ["[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")","[","Ni3"," ","jin1","!","\"","\'","\n","\t","{","[","(","tian1"," ","hai2"," ","you3"," ","ke4"," ","ma","?"," ","(","Wo3"," ","méi","yǒu",".",")"]
		self.assertEquals(self.pinyin_parser_mixed.fastParse(long_string), long_text_components)
		
		
	def test_getAllVariantsOfSyllable (self):
		
		ni_variations = ["ni", "Ni", "ni0", "ni1", "ni2", "ni3", "ni4", "Ni0", "Ni1", "Ni2", "Ni3", "Ni4", "nī", "ní", "nǐ", "nì", "Nī", "Ní", "Nǐ", "Nì"]
		hao_variations = ["hao", "Hao", "hao0", "hao1", "hao2", "hao3", "hao4", "Hao0", "Hao1", "Hao2", "Hao3", "Hao4", "hāo", "háo", "hǎo", "hào", "Hāo", "Háo", "Hǎo", "Hào"]
		ma_variations = ["ma", "Ma", "ma0", "ma1", "ma2", "ma3", "ma4", "Ma0", "Ma1", "Ma2", "Ma3", "Ma4", "mā", "má", "mǎ", "mà", "Mā", "Má", "Mǎ", "Mà"]
		
		self.assertEquals(self.pinyin_parser_mixed.getAllVariantsOfPlainSyllable("ni"), ni_variations)
		self.assertEquals(self.pinyin_parser_mixed.getAllVariantsOfPlainSyllable("hao"), hao_variations)
		self.assertEquals(self.pinyin_parser_mixed.getAllVariantsOfPlainSyllable("ma"), ma_variations)
		
	def test_getNumberedVariantsOfPlainSyllable(self):
		
		numbered_ni_variations = ["ni0", "ni1", "ni2", "ni3", "ni4", "Ni0", "Ni1", "Ni2", "Ni3", "Ni4"]
		numbered_hao_variations = ["hao0", "hao1", "hao2", "hao3", "hao4", "Hao0", "Hao1", "Hao2", "Hao3", "Hao4"]
		numbered_ma_variations = ["ma0", "ma1", "ma2", "ma3", "ma4", "Ma0", "Ma1", "Ma2", "Ma3", "Ma4"]
		
		self.assertEquals(self.pinyin_parser_mixed.getNumberedVariantsOfPlainSyllable("ni"), numbered_ni_variations)
		self.assertEquals(self.pinyin_parser_mixed.getNumberedVariantsOfPlainSyllable("hao"), numbered_hao_variations)
		self.assertEquals(self.pinyin_parser_mixed.getNumberedVariantsOfPlainSyllable("ma"), numbered_ma_variations)
		
		self.assertEquals(self.pinyin_parser_mixed.getNumberedVariantsOfPlainSyllable("Ni"), numbered_ni_variations)
		self.assertEquals(self.pinyin_parser_mixed.getNumberedVariantsOfPlainSyllable("Hao"), numbered_hao_variations)
		self.assertEquals(self.pinyin_parser_mixed.getNumberedVariantsOfPlainSyllable("Ma"), numbered_ma_variations)
	
	def test_getTonedVariantsOfPlainSyllable(self):
		self.assertEquals(self.pinyin_parser_mixed.getTonedVariantsOfPlainSyllable("ni"), ["nī", "ní", "nǐ", "nì", "Nī", "Ní", "Nǐ", "Nì"])
		self.assertEquals(self.pinyin_parser_mixed.getTonedVariantsOfPlainSyllable("hao"), ["hāo", "háo", "hǎo", "hào", "Hāo", "Háo", "Hǎo", "Hào"])
		self.assertEquals(self.pinyin_parser_mixed.getTonedVariantsOfPlainSyllable("ma"), ["mā", "má", "mǎ", "mà", "Mā", "Má", "Mǎ", "Mà"])
		
		self.assertEquals(self.pinyin_parser_mixed.getTonedVariantsOfPlainSyllable("Ni"), ["nī", "ní", "nǐ", "nì", "Nī", "Ní", "Nǐ", "Nì"])
		self.assertEquals(self.pinyin_parser_mixed.getTonedVariantsOfPlainSyllable("Hao"), ["hāo", "háo", "hǎo", "hào", "Hāo", "Háo", "Hǎo", "Hào"])
		self.assertEquals(self.pinyin_parser_mixed.getTonedVariantsOfPlainSyllable("Ma"), ["mā", "má", "mǎ", "mà", "Mā", "Má", "Mǎ", "Mà"])
		
	def test_getPlainVariantsOfPlainSyllable(self):
		self.assertEquals(self.pinyin_parser_mixed.getPlainVariantsOfPlainSyllable("ni"), ["ni", "Ni"])
		self.assertEquals(self.pinyin_parser_mixed.getPlainVariantsOfPlainSyllable("hao"), ["hao", "Hao"])
		self.assertEquals(self.pinyin_parser_mixed.getPlainVariantsOfPlainSyllable("ma"), ["ma", "Ma"])
		
		self.assertEquals(self.pinyin_parser_mixed.getPlainVariantsOfPlainSyllable("Ni"), ["ni", "Ni"])
		self.assertEquals(self.pinyin_parser_mixed.getPlainVariantsOfPlainSyllable("Hao"), ["hao", "Hao"])
		self.assertEquals(self.pinyin_parser_mixed.getPlainVariantsOfPlainSyllable("Ma"), ["ma", "Ma"])
	
	def test_isPinyinSyllable (self):
		self.assertTrue(self.pinyin_parser_mixed.isPinyinSyllable("zao"))
		self.assertTrue(self.pinyin_parser_mixed.isPinyinSyllable("zao3"))
		self.assertTrue(self.pinyin_parser_mixed.isPinyinSyllable("zǎo"))
		self.assertTrue(self.pinyin_parser_mixed.isPinyinSyllable("Zao"))
		self.assertTrue(self.pinyin_parser_mixed.isPinyinSyllable("Zao3"))
		self.assertTrue(self.pinyin_parser_mixed.isPinyinSyllable("Zǎo"))
		
		self.assertTrue(self.pinyin_parser_mixed.isPinyinSyllable("shang"))
		self.assertTrue(self.pinyin_parser_mixed.isPinyinSyllable("shang4"))
		self.assertTrue(self.pinyin_parser_mixed.isPinyinSyllable("shàng"))
		self.assertTrue(self.pinyin_parser_mixed.isPinyinSyllable("Shang"))
		self.assertTrue(self.pinyin_parser_mixed.isPinyinSyllable("Shang4"))
		self.assertTrue(self.pinyin_parser_mixed.isPinyinSyllable("Shàng"))
		
		self.assertTrue(self.pinyin_parser_mixed.isPinyinSyllable("hao"))
		self.assertTrue(self.pinyin_parser_mixed.isPinyinSyllable("hao3"))
		self.assertTrue(self.pinyin_parser_mixed.isPinyinSyllable("hǎo"))
		self.assertTrue(self.pinyin_parser_mixed.isPinyinSyllable("Hao"))
		self.assertTrue(self.pinyin_parser_mixed.isPinyinSyllable("Hao3"))
		self.assertTrue(self.pinyin_parser_mixed.isPinyinSyllable("Hǎo"))
		
		self.assertFalse(self.pinyin_parser_mixed.isPinyinSyllable("pun"))
		self.assertFalse(self.pinyin_parser_mixed.isPinyinSyllable("pun0"))
		self.assertFalse(self.pinyin_parser_mixed.isPinyinSyllable("pun1"))
		self.assertFalse(self.pinyin_parser_mixed.isPinyinSyllable("pun2"))
		self.assertFalse(self.pinyin_parser_mixed.isPinyinSyllable("pun3"))
		self.assertFalse(self.pinyin_parser_mixed.isPinyinSyllable("pun4"))
		self.assertFalse(self.pinyin_parser_mixed.isPinyinSyllable("pūn"))
		self.assertFalse(self.pinyin_parser_mixed.isPinyinSyllable("pún"))
		self.assertFalse(self.pinyin_parser_mixed.isPinyinSyllable("pǔn"))
		self.assertFalse(self.pinyin_parser_mixed.isPinyinSyllable("pùn"))
		self.assertFalse(self.pinyin_parser_mixed.isPinyinSyllable("Pun"))
		
		self.assertFalse(self.pinyin_parser_mixed.isPinyinSyllable("Pun"))
		self.assertFalse(self.pinyin_parser_mixed.isPinyinSyllable("Pun0"))
		self.assertFalse(self.pinyin_parser_mixed.isPinyinSyllable("Pun1"))
		self.assertFalse(self.pinyin_parser_mixed.isPinyinSyllable("Pun2"))
		self.assertFalse(self.pinyin_parser_mixed.isPinyinSyllable("Pun3"))
		self.assertFalse(self.pinyin_parser_mixed.isPinyinSyllable("Pun4"))
		self.assertFalse(self.pinyin_parser_mixed.isPinyinSyllable("Pūn"))
		self.assertFalse(self.pinyin_parser_mixed.isPinyinSyllable("Pún"))
		self.assertFalse(self.pinyin_parser_mixed.isPinyinSyllable("Pǔn"))
		self.assertFalse(self.pinyin_parser_mixed.isPinyinSyllable("Pùn"))
	
	def test_removeValidNonSyllableCharacters_writes_to_list (self):
		
		# test adds to not empty list using numbers
		self.pinyin_parser_mixed.text_components = ["Ni3", "hao3", "ma", "?"]
		self.pinyin_parser_mixed.removeValidNonSyllableCharacters("([{,...…-Wo3 jin1tian1 hen3mang2.")
		self.assertEquals(self.pinyin_parser_mixed.text_components, ["Ni3", "hao3", "ma", "?", "(", "[", "{", ",", ".", ".", ".", "…", "-"])
		
		# test adds to not empty list using tones
		self.pinyin_parser_mixed.text_components = ["Ni3", "hao3", "ma", "?"]
		self.pinyin_parser_mixed.removeValidNonSyllableCharacters("([{,...…-Wǒ jīntiān hěnmáng.")
		self.assertEquals(self.pinyin_parser_mixed.text_components, ["Ni3", "hao3", "ma", "?", "(", "[", "{", ",", ".", ".", ".", "…", "-"])
		
		# test adds to empty list using numbers
		self.pinyin_parser_mixed.text_components = []
		self.pinyin_parser_mixed.removeValidNonSyllableCharacters("([{,...…-Wo3 jin1tian1 hen3mang2.")
		self.assertEquals(self.pinyin_parser_mixed.text_components, ["(", "[", "{", ",", ".", ".", ".", "…", "-"])
		
		# test adds to empty list using tones
		self.pinyin_parser_mixed.text_components = []
		self.pinyin_parser_mixed.removeValidNonSyllableCharacters("([{,...…-Wǒ jīntiān hěnmáng.")
		self.assertEquals(self.pinyin_parser_mixed.text_components, ["(", "[", "{", ",", ".", ".", ".", "…", "-"])
		
		# test adds nothing to not empty list using numbers
		self.pinyin_parser_mixed.text_components = ["Ni3", "hao3", "ma", "?"]
		self.pinyin_parser_mixed.removeValidNonSyllableCharacters("Wo3 jin1tian1 hen3mang2.")
		self.assertEquals(self.pinyin_parser_mixed.text_components, ["Ni3", "hao3", "ma", "?"])
		
		# test adds nothing to not empty list using tones
		self.pinyin_parser_mixed.text_components = ["Ni3", "hao3", "ma", "?"]
		self.pinyin_parser_mixed.removeValidNonSyllableCharacters("Wǒ jīntiān hěnmáng.")
		self.assertEquals(self.pinyin_parser_mixed.text_components, ["Ni3", "hao3", "ma", "?"])
		
		# test adds nothing to empty list using numbers
		self.pinyin_parser_mixed.text_components = []
		self.pinyin_parser_mixed.removeValidNonSyllableCharacters("Wo3 jin1tian1 hen3mang2.")
		self.assertEquals(self.pinyin_parser_mixed.text_components, [])
		
		# test adds nothing to empty list using tones
		self.pinyin_parser_mixed.text_components = []
		self.pinyin_parser_mixed.removeValidNonSyllableCharacters("Wǒ jīntiān hěnmáng.")
		self.assertEquals(self.pinyin_parser_mixed.text_components, [])
		
		# test multiple calls on empty list
		self.pinyin_parser_mixed.text_components = []
		self.pinyin_parser_mixed.removeValidNonSyllableCharacters("Wǒ jīntiān hěnmáng.")
		self.pinyin_parser_mixed.removeValidNonSyllableCharacters("-…,;:Wǒ jīntiān hěnmáng.")
		self.assertEquals(self.pinyin_parser_mixed.text_components, ["-","…",",",";",":"])
		
		self.pinyin_parser_mixed.text_components = []
		self.pinyin_parser_mixed.removeValidNonSyllableCharacters("-…,Wǒ jīntiān hěnmáng.")
		self.pinyin_parser_mixed.removeValidNonSyllableCharacters(";:Wǒ jīntiān hěnmáng.")
		self.assertEquals(self.pinyin_parser_mixed.text_components, ["-","…",",",";",":"])
		
		# test multiple calls on not empty list
		self.pinyin_parser_mixed.text_components = ["ni3"]
		self.pinyin_parser_mixed.removeValidNonSyllableCharacters("Wǒ jīntiān hěnmáng.")
		self.pinyin_parser_mixed.removeValidNonSyllableCharacters("-…,;:Wǒ jīntiān hěnmáng.")
		self.assertEquals(self.pinyin_parser_mixed.text_components, ["ni3","-","…",",",";",":"])
		
		self.pinyin_parser_mixed.text_components = ["ni3"]
		self.pinyin_parser_mixed.removeValidNonSyllableCharacters("-…,Wǒ jīntiān hěnmáng.")
		self.pinyin_parser_mixed.removeValidNonSyllableCharacters(";:Wǒ jīntiān hěnmáng.")
		self.assertEquals(self.pinyin_parser_mixed.text_components, ["ni3","-","…",",",";",":"])
		
	def test_removeValidNonSyllableCharacters_removes_from_text (self):
		self.assertEquals(self.pinyin_parser_mixed.removeValidNonSyllableCharacters("-…,Wǒ jīntiān hěnmáng."), "Wǒ jīntiān hěnmáng.")
		self.assertEquals(self.pinyin_parser_mixed.removeValidNonSyllableCharacters("012345Wǒ jīntiān hěnmáng."), "Wǒ jīntiān hěnmáng.")
		self.assertEquals(self.pinyin_parser_mixed.removeValidNonSyllableCharacters("0Wǒ jīntiān hěnmáng."), "Wǒ jīntiān hěnmáng.")
		self.assertEquals(self.pinyin_parser_mixed.removeValidNonSyllableCharacters("1Wǒ jīntiān hěnmáng."), "Wǒ jīntiān hěnmáng.")
		self.assertEquals(self.pinyin_parser_mixed.removeValidNonSyllableCharacters("2Wǒ jīntiān hěnmáng."), "Wǒ jīntiān hěnmáng.")
		self.assertEquals(self.pinyin_parser_mixed.removeValidNonSyllableCharacters("3Wǒ jīntiān hěnmáng."), "Wǒ jīntiān hěnmáng.")
		self.assertEquals(self.pinyin_parser_mixed.removeValidNonSyllableCharacters("4Wǒ jīntiān hěnmáng."), "Wǒ jīntiān hěnmáng.")
		self.assertEquals(self.pinyin_parser_mixed.removeValidNonSyllableCharacters("4!?.Wǒ jīntiān hěnmáng."), "Wǒ jīntiān hěnmáng.")
	
	def test_addPlainSyllableToTextComponents(self):
		# add to empty list
		self.pinyin_parser_mixed.text_components = []
		self.pinyin_parser_mixed.addPlainSyllableToTextComponents("ni")
		self.pinyin_parser_mixed.addPlainSyllableToTextComponents("hao")
		self.pinyin_parser_mixed.addPlainSyllableToTextComponents("ma")
		self.assertEquals(self.pinyin_parser_mixed.text_components, ["ni", "hao", "ma"])
		
		self.assertEquals(self.pinyin_parser_mixed.is_text_component_toned_syllable_dictionary, {0:False, 1:False, 2:False})
		self.assertEquals(self.pinyin_parser_mixed.is_text_component_numbered_syllable_dictionary, {0:False, 1:False, 2:False})
		self.assertEquals(self.pinyin_parser_mixed.is_text_component_plain_syllable_dictionary, {0:True, 1:True, 2:True})
		# add to not empty list
		self.pinyin_parser_mixed.text_components = ["Ni3", "hao3", "ma", "?"]
		
		self.pinyin_parser_mixed.is_text_component_toned_syllable_dictionary = {0:False, 1:False, 2:False, 3:False}
		self.pinyin_parser_mixed.is_text_component_numbered_syllable_dictionary = {0:True, 1:True, 2:False, 3:False}
		self.pinyin_parser_mixed.is_text_component_plain_syllable_dictionary = {0:False, 1:False, 2:True, 3:False}
		
		self.pinyin_parser_mixed.addPlainSyllableToTextComponents("ni")
		self.pinyin_parser_mixed.addPlainSyllableToTextComponents("hao")
		self.pinyin_parser_mixed.addPlainSyllableToTextComponents("ma")
		self.assertEquals(self.pinyin_parser_mixed.text_components, ["Ni3", "hao3", "ma", "?", "ni", "hao", "ma"])
		
		self.assertEquals(self.pinyin_parser_mixed.is_text_component_toned_syllable_dictionary, {0:False, 1:False, 2:False, 3:False, 4:False, 5:False, 6:False})
		self.assertEquals(self.pinyin_parser_mixed.is_text_component_numbered_syllable_dictionary, {0:True, 1:True, 2:False, 3:False, 4:False, 5:False, 6:False})
		self.assertEquals(self.pinyin_parser_mixed.is_text_component_plain_syllable_dictionary, {0:False, 1:False, 2:True, 3:False, 4:True, 5:True, 6:True})
	
	def test_addNumberedSyllableToTextComponents(self):
		# add to empty list
		self.pinyin_parser_mixed.text_components = []
		self.pinyin_parser_mixed.addNumberedSyllableToTextComponents("zao3")
		self.pinyin_parser_mixed.addNumberedSyllableToTextComponents("shang4")
		self.pinyin_parser_mixed.addNumberedSyllableToTextComponents("hao3")
		self.assertEquals(self.pinyin_parser_mixed.text_components, ["zao3", "shang4", "hao3"])
		
		self.assertEquals(self.pinyin_parser_mixed.is_text_component_toned_syllable_dictionary, {0:False, 1:False, 2:False})
		self.assertEquals(self.pinyin_parser_mixed.is_text_component_numbered_syllable_dictionary, {0:True, 1:True, 2:True})
		self.assertEquals(self.pinyin_parser_mixed.is_text_component_plain_syllable_dictionary, {0:False, 1:False, 2:False})
		
		# add to not empty list
		self.pinyin_parser_mixed.text_components = ["Ni3", "hao3", "ma", "?"]
		self.pinyin_parser_mixed.is_text_component_toned_syllable_dictionary = {0:False, 1:False, 2:False, 3:False}
		self.pinyin_parser_mixed.is_text_component_numbered_syllable_dictionary = {0:True, 1:True, 2:False, 3:False}
		self.pinyin_parser_mixed.is_text_component_plain_syllable_dictionary = {0:False, 1:False, 2:True, 3:False}
		self.pinyin_parser_mixed.addNumberedSyllableToTextComponents("zao3")
		self.pinyin_parser_mixed.addNumberedSyllableToTextComponents("shang4")
		self.pinyin_parser_mixed.addNumberedSyllableToTextComponents("hao3")
		self.assertEquals(self.pinyin_parser_mixed.text_components, ["Ni3", "hao3", "ma", "?", "zao3", "shang4", "hao3"])
		
		self.assertEquals(self.pinyin_parser_mixed.is_text_component_toned_syllable_dictionary, {0:False, 1:False, 2:False, 3:False, 4:False, 5:False, 6:False})
		self.assertEquals(self.pinyin_parser_mixed.is_text_component_numbered_syllable_dictionary, {0:True, 1:True, 2:False, 3:False, 4:True, 5:True, 6:True})
		self.assertEquals(self.pinyin_parser_mixed.is_text_component_plain_syllable_dictionary, {0:False, 1:False, 2:True, 3:False, 4:False, 5:False, 6:False})
	
	def test_addTonedSyllableToTextComponents(self):
		# add to empty list
		self.pinyin_parser_mixed.text_components = []
		self.pinyin_parser_mixed.addTonedSyllableToTextComponents("zǎo")
		self.pinyin_parser_mixed.addTonedSyllableToTextComponents("shàng")
		self.pinyin_parser_mixed.addTonedSyllableToTextComponents("hǎo")
		self.assertEquals(self.pinyin_parser_mixed.text_components, ["zǎo", "shàng", "hǎo"])

		self.assertEquals(self.pinyin_parser_mixed.is_text_component_toned_syllable_dictionary, {0:True, 1:True, 2:True})
		self.assertEquals(self.pinyin_parser_mixed.is_text_component_numbered_syllable_dictionary, {0:False, 1:False, 2:False})
		self.assertEquals(self.pinyin_parser_mixed.is_text_component_plain_syllable_dictionary, {0:False, 1:False, 2:False})

		# add to not empty list
		self.pinyin_parser_mixed.text_components = ["Ni3", "hao3", "ma", "?"]
		self.pinyin_parser_mixed.is_text_component_toned_syllable_dictionary = {0:False, 1:False, 2:False, 3:False}
		self.pinyin_parser_mixed.is_text_component_numbered_syllable_dictionary = {0:True, 1:True, 2:False, 3:False}
		self.pinyin_parser_mixed.is_text_component_plain_syllable_dictionary = {0:False, 1:False, 2:True, 3:False}
		self.pinyin_parser_mixed.addTonedSyllableToTextComponents("zǎo")
		self.pinyin_parser_mixed.addTonedSyllableToTextComponents("shàng")
		self.pinyin_parser_mixed.addTonedSyllableToTextComponents("hǎo")
		self.assertEquals(self.pinyin_parser_mixed.text_components, ["Ni3", "hao3", "ma", "?", "zǎo", "shàng", "hǎo"])
		
		self.assertEquals(self.pinyin_parser_mixed.is_text_component_toned_syllable_dictionary, {0:False, 1:False, 2:False, 3:False, 4:True, 5:True, 6:True})
		self.assertEquals(self.pinyin_parser_mixed.is_text_component_numbered_syllable_dictionary, {0:True, 1:True, 2:False, 3:False, 4:False, 5:False, 6:False})
		self.assertEquals(self.pinyin_parser_mixed.is_text_component_plain_syllable_dictionary, {0:False, 1:False, 2:True, 3:False, 4:False, 5:False, 6:False})
	
	def test_addNonSyllableCharacterToTextComponents (self):
		# add to empty list
		self.pinyin_parser_mixed.text_components = []
		self.pinyin_parser_mixed.addNonSyllableCharacterToTextComponents("…")
		self.pinyin_parser_mixed.addNonSyllableCharacterToTextComponents("?")
		self.pinyin_parser_mixed.addNonSyllableCharacterToTextComponents("!")
		self.pinyin_parser_mixed.addNonSyllableCharacterToTextComponents(".")
		self.assertEquals(self.pinyin_parser_mixed.text_components, ["…", "?", "!", "."])
		# add to not empty list
		self.pinyin_parser_mixed.text_components = ["Ni3", "hao3", "ma", "?"]
		self.pinyin_parser_mixed.addNonSyllableCharacterToTextComponents("…")
		self.pinyin_parser_mixed.addNonSyllableCharacterToTextComponents("?")
		self.pinyin_parser_mixed.addNonSyllableCharacterToTextComponents("!")
		self.pinyin_parser_mixed.addNonSyllableCharacterToTextComponents(".")
		self.assertEquals(self.pinyin_parser_mixed.text_components, ["Ni3", "hao3", "ma", "?", "…", "?", "!", "."])
		
	def test_getNumberedPinyinText(self):
		self.pinyin_parser_mixed.text_components = ["Ni3", "hao3", "ma", "?"]
		self.pinyin_parser_mixed.is_text_component_plain_syllable_dictionary = {0:False, 1:False, 2:True, 3:False}
		self.pinyin_parser_mixed.is_text_component_numbered_syllable_dictionary = {0:True, 1:True, 2:False, 3:False}
		self.pinyin_parser_mixed.is_text_component_toned_syllable_dictionary = {0:False, 1:False, 2:False, 3:False}
		
		self.assertEquals(self.pinyin_parser_mixed.getNumberedPinyinText(), "Ni3hao3ma?")
		
		self.pinyin_parser_mixed.text_components = ["Nǐ","hǎo","ma","?"]
		self.pinyin_parser_mixed.is_text_component_plain_syllable_dictionary = {0:False, 1:False, 2:True, 3:False}
		self.pinyin_parser_mixed.is_text_component_numbered_syllable_dictionary = {0:False, 1:False, 2:False, 3:False}
		self.pinyin_parser_mixed.is_text_component_toned_syllable_dictionary = {0:True, 1:True, 2:False, 3:False}
		
		self.assertEquals(self.pinyin_parser_mixed.getNumberedPinyinText(), "Ni3hao3ma?")
		
		numbered_components = ["Ming2","tian1","ni3","!","dei3","?","qi3"," ","chuang1","hen3","zao3","."," ","Wan3","an1","!"]
		toned_components = ["Míng","tiān","nǐ","!","děi","?","qǐ"," ","chuāng","hěn","zǎo","."," ","Wǎn","ān","!"]
		numbered_text = "Ming2tian1ni3!dei3?qi3 chuang1hen3zao3. Wan3an1!"
		
		self.pinyin_parser_mixed.text_components = numbered_components
		plain_dict = {0:False, 1:False, 2:False, 3:False, 4:False, 5:False, 6:False, 7:False, 8:False, 9:False, 10:False, 11:False, 12:False, 13:False, 14:False, 15:False}
		numbered_dict = {0:True, 1:True, 2:True, 3:False, 4:True, 5:False, 6:True, 7:False, 8:True, 9:True, 10:True, 11:False, 12:False, 13:True, 14:True, 15:False}
		toned_dict = {0:False, 1:False, 2:False, 3:False, 4:False, 5:False, 6:False, 7:False, 8:False, 9:False, 10:False, 11:False, 12:False, 13:False, 14:False, 15:False}
		self.pinyin_parser_mixed.is_text_component_plain_syllable_dictionary = plain_dict
		self.pinyin_parser_mixed.is_text_component_numbered_syllable_dictionary = numbered_dict
		self.pinyin_parser_mixed.is_text_component_toned_syllable_dictionary = toned_dict
		
		self.assertEquals(self.pinyin_parser_mixed.getNumberedPinyinText(), numbered_text)
		
		self.pinyin_parser_mixed.text_components = toned_components
		plain_dict = {0:False, 1:False, 2:False, 3:False, 4:False, 5:False, 6:False, 7:False, 8:False, 9:False, 10:False, 11:False, 12:False, 13:False, 14:False, 15:False}
		numbered_dict = {0:False, 1:False, 2:False, 3:False, 4:False, 5:False, 6:False, 7:False, 8:False, 9:False, 10:False, 11:False, 12:False, 13:False, 14:False, 15:False}
		toned_dict = {0:True, 1:True, 2:True, 3:False, 4:True, 5:False, 6:True, 7:False, 8:True, 9:True, 10:True, 11:False, 12:False, 13:True, 14:True, 15:False}
		self.pinyin_parser_mixed.is_text_component_plain_syllable_dictionary = plain_dict
		self.pinyin_parser_mixed.is_text_component_numbered_syllable_dictionary = numbered_dict
		self.pinyin_parser_mixed.is_text_component_toned_syllable_dictionary = toned_dict
		
		self.assertEquals(self.pinyin_parser_mixed.getNumberedPinyinText(), numbered_text)
		
	def test_getTonedPinyinText(self):
		self.pinyin_parser_mixed.text_components = ["Ni3", "hao3", "ma", "?"]
		
		self.pinyin_parser_mixed.is_text_component_plain_syllable_dictionary = {0:False, 1:False, 2:True, 3:False}
		self.pinyin_parser_mixed.is_text_component_numbered_syllable_dictionary = {0:True, 1:True, 2:False, 3:False}
		self.pinyin_parser_mixed.is_text_component_toned_syllable_dictionary = {0:False, 1:False, 2:False, 3:False}
		
		self.assertEquals(self.pinyin_parser_mixed.getTonedPinyinText(), "Nǐhǎoma?")
		
		self.pinyin_parser_mixed.is_text_component_plain_syllable_dictionary = {0:False, 1:False, 2:True, 3:False}
		self.pinyin_parser_mixed.is_text_component_numbered_syllable_dictionary = {0:False, 1:False, 2:False, 3:False}
		self.pinyin_parser_mixed.is_text_component_toned_syllable_dictionary = {0:True, 1:True, 2:False, 3:False}
		
		self.pinyin_parser_mixed.text_components = ["Nǐ","hǎo","ma","?"]
		
		self.assertEquals(self.pinyin_parser_mixed.getTonedPinyinText(), "Nǐhǎoma?")
		
		numbered_components = ["Ming2","tian1","ni3","!","dei3","?","qi3"," ","chuang1","hen3","zao3","."," ","Wan3","an1","!"]
		toned_components = ["Míng","tiān","nǐ","!","děi","?","qǐ"," ","chuāng","hěn","zǎo","."," ","Wǎn","ān","!"]
		toned_text = "Míngtiānnǐ!děi?qǐ chuānghěnzǎo. Wǎnān!"
		
		plain_dict = {0:False, 1:False, 2:False, 3:False, 4:False, 5:False, 6:False, 7:False, 8:False, 9:False, 10:False, 11:False, 12:False, 13:False, 14:False, 15:False}
		numbered_dict = {0:True, 1:True, 2:True, 3:False, 4:True, 5:False, 6:True, 7:False, 8:True, 9:True, 10:True, 11:False, 12:False, 13:True, 14:True, 15:False}
		toned_dict = {0:False, 1:False, 2:False, 3:False, 4:False, 5:False, 6:False, 7:False, 8:False, 9:False, 10:False, 11:False, 12:False, 13:False, 14:False, 15:False}
		
		self.pinyin_parser_mixed.is_text_component_plain_syllable_dictionary = plain_dict
		self.pinyin_parser_mixed.is_text_component_numbered_syllable_dictionary = numbered_dict
		self.pinyin_parser_mixed.is_text_component_toned_syllable_dictionary = toned_dict
		
		self.pinyin_parser_mixed.text_components = numbered_components
		
		self.assertEquals(self.pinyin_parser_mixed.getTonedPinyinText(), toned_text)
		
		self.pinyin_parser_mixed.text_components = toned_components
		
		plain_dict = {0:False, 1:False, 2:False, 3:False, 4:False, 5:False, 6:False, 7:False, 8:False, 9:False, 10:False, 11:False, 12:False, 13:False, 14:False, 15:False}
		numbered_dict = {0:False, 1:False, 2:False, 3:False, 4:False, 5:False, 6:False, 7:False, 8:False, 9:False, 10:False, 11:False, 12:False, 13:False, 14:False, 15:False}
		toned_dict = {0:True, 1:True, 2:True, 3:False, 4:True, 5:False, 6:True, 7:False, 8:True, 9:True, 10:True, 11:False, 12:False, 13:True, 14:True, 15:False}
		
		self.pinyin_parser_mixed.is_text_component_plain_syllable_dictionary = plain_dict
		self.pinyin_parser_mixed.is_text_component_numbered_syllable_dictionary = numbered_dict
		self.pinyin_parser_mixed.is_text_component_toned_syllable_dictionary = toned_dict
		
		self.assertEquals(self.pinyin_parser_mixed.getTonedPinyinText(), toned_text)
	
	def test_getTonedSyllableFromSyllableAndToneNumber (self):
		self.assertEquals(self.pinyin_parser_mixed.getTonedSyllableFromPlainSyllableAndToneNumber("Ni", 3), "Nǐ")
		self.assertEquals(self.pinyin_parser_mixed.getTonedSyllableFromPlainSyllableAndToneNumber("ni", 3), "nǐ")

		self.assertEquals(self.pinyin_parser_mixed.getTonedSyllableFromPlainSyllableAndToneNumber("Hao", 3), "Hǎo")
		self.assertEquals(self.pinyin_parser_mixed.getTonedSyllableFromPlainSyllableAndToneNumber("hao", 3), "hǎo")

		self.assertEquals(self.pinyin_parser_mixed.getTonedSyllableFromPlainSyllableAndToneNumber("Ma", 0), "Ma")
		self.assertEquals(self.pinyin_parser_mixed.getTonedSyllableFromPlainSyllableAndToneNumber("ma", 0), "ma")
		
		self.assertEquals(self.pinyin_parser_mixed.getTonedSyllableFromPlainSyllableAndToneNumber("Zhe", 4), "Zhè")
		self.assertEquals(self.pinyin_parser_mixed.getTonedSyllableFromPlainSyllableAndToneNumber("zhe", 4), "zhè")

		self.assertEquals(self.pinyin_parser_mixed.getTonedSyllableFromPlainSyllableAndToneNumber("Shi", 4), "Shì")
		self.assertEquals(self.pinyin_parser_mixed.getTonedSyllableFromPlainSyllableAndToneNumber("shi", 4), "shì")

		self.assertEquals(self.pinyin_parser_mixed.getTonedSyllableFromPlainSyllableAndToneNumber("Yi", 1), "Yī")
		self.assertEquals(self.pinyin_parser_mixed.getTonedSyllableFromPlainSyllableAndToneNumber("yi", 1), "yī")

		self.assertEquals(self.pinyin_parser_mixed.getTonedSyllableFromPlainSyllableAndToneNumber("Wei", 4), "Wèi")
		self.assertEquals(self.pinyin_parser_mixed.getTonedSyllableFromPlainSyllableAndToneNumber("wei", 4), "wèi")

		self.assertEquals(self.pinyin_parser_mixed.getTonedSyllableFromPlainSyllableAndToneNumber("Jiao", 4), "Jiào")
		self.assertEquals(self.pinyin_parser_mixed.getTonedSyllableFromPlainSyllableAndToneNumber("jiao", 4), "jiào")

		self.assertEquals(self.pinyin_parser_mixed.getTonedSyllableFromPlainSyllableAndToneNumber("Shou", 4), "Shòu")
		self.assertEquals(self.pinyin_parser_mixed.getTonedSyllableFromPlainSyllableAndToneNumber("shou", 4), "shòu")
	
	def test_getTonedVocalFromVocalAndToneNumber (self):
		self.assertEquals(self.pinyin_parser_mixed.getTonedVocalFromVocalAndToneNumber("a", 0), "a")
		self.assertEquals(self.pinyin_parser_mixed.getTonedVocalFromVocalAndToneNumber("a", 1), "ā")
		self.assertEquals(self.pinyin_parser_mixed.getTonedVocalFromVocalAndToneNumber("a", 2), "á")
		self.assertEquals(self.pinyin_parser_mixed.getTonedVocalFromVocalAndToneNumber("a", 3), "ǎ")
		self.assertEquals(self.pinyin_parser_mixed.getTonedVocalFromVocalAndToneNumber("a", 4), "à")
		
		self.assertEquals(self.pinyin_parser_mixed.getTonedVocalFromVocalAndToneNumber("A", 0), "A")
		self.assertEquals(self.pinyin_parser_mixed.getTonedVocalFromVocalAndToneNumber("A", 1), "Ā")
		self.assertEquals(self.pinyin_parser_mixed.getTonedVocalFromVocalAndToneNumber("A", 2), "Á")
		self.assertEquals(self.pinyin_parser_mixed.getTonedVocalFromVocalAndToneNumber("A", 3), "Ǎ")
		self.assertEquals(self.pinyin_parser_mixed.getTonedVocalFromVocalAndToneNumber("A", 4), "À")
		
		self.assertEquals(self.pinyin_parser_mixed.getTonedVocalFromVocalAndToneNumber("e", 0), "e")
		self.assertEquals(self.pinyin_parser_mixed.getTonedVocalFromVocalAndToneNumber("e", 1), "ē")
		self.assertEquals(self.pinyin_parser_mixed.getTonedVocalFromVocalAndToneNumber("e", 2), "é")
		self.assertEquals(self.pinyin_parser_mixed.getTonedVocalFromVocalAndToneNumber("e", 3), "ě")
		self.assertEquals(self.pinyin_parser_mixed.getTonedVocalFromVocalAndToneNumber("e", 4), "è")
		
		self.assertEquals(self.pinyin_parser_mixed.getTonedVocalFromVocalAndToneNumber("E", 0), "E")
		self.assertEquals(self.pinyin_parser_mixed.getTonedVocalFromVocalAndToneNumber("E", 1), "Ē")
		self.assertEquals(self.pinyin_parser_mixed.getTonedVocalFromVocalAndToneNumber("E", 2), "É")
		self.assertEquals(self.pinyin_parser_mixed.getTonedVocalFromVocalAndToneNumber("E", 3), "Ě")
		self.assertEquals(self.pinyin_parser_mixed.getTonedVocalFromVocalAndToneNumber("E", 4), "È")
		
		self.assertEquals(self.pinyin_parser_mixed.getTonedVocalFromVocalAndToneNumber("i", 0), "i")
		self.assertEquals(self.pinyin_parser_mixed.getTonedVocalFromVocalAndToneNumber("i", 1), "ī")
		self.assertEquals(self.pinyin_parser_mixed.getTonedVocalFromVocalAndToneNumber("i", 2), "í")
		self.assertEquals(self.pinyin_parser_mixed.getTonedVocalFromVocalAndToneNumber("i", 3), "ǐ")
		self.assertEquals(self.pinyin_parser_mixed.getTonedVocalFromVocalAndToneNumber("i", 4), "ì")
		
		self.assertEquals(self.pinyin_parser_mixed.getTonedVocalFromVocalAndToneNumber("I", 0), "I")
		self.assertEquals(self.pinyin_parser_mixed.getTonedVocalFromVocalAndToneNumber("I", 1), "Ī")
		self.assertEquals(self.pinyin_parser_mixed.getTonedVocalFromVocalAndToneNumber("I", 2), "Í")
		self.assertEquals(self.pinyin_parser_mixed.getTonedVocalFromVocalAndToneNumber("I", 3), "Ǐ")
		self.assertEquals(self.pinyin_parser_mixed.getTonedVocalFromVocalAndToneNumber("I", 4), "Ì")
		
		self.assertEquals(self.pinyin_parser_mixed.getTonedVocalFromVocalAndToneNumber("o", 0), "o")
		self.assertEquals(self.pinyin_parser_mixed.getTonedVocalFromVocalAndToneNumber("o", 1), "ō")
		self.assertEquals(self.pinyin_parser_mixed.getTonedVocalFromVocalAndToneNumber("o", 2), "ó")
		self.assertEquals(self.pinyin_parser_mixed.getTonedVocalFromVocalAndToneNumber("o", 3), "ǒ")
		self.assertEquals(self.pinyin_parser_mixed.getTonedVocalFromVocalAndToneNumber("o", 4), "ò")
		
		self.assertEquals(self.pinyin_parser_mixed.getTonedVocalFromVocalAndToneNumber("O", 0), "O")
		self.assertEquals(self.pinyin_parser_mixed.getTonedVocalFromVocalAndToneNumber("O", 1), "Ō")
		self.assertEquals(self.pinyin_parser_mixed.getTonedVocalFromVocalAndToneNumber("O", 2), "Ó")
		self.assertEquals(self.pinyin_parser_mixed.getTonedVocalFromVocalAndToneNumber("O", 3), "Ǒ")
		self.assertEquals(self.pinyin_parser_mixed.getTonedVocalFromVocalAndToneNumber("O", 4), "Ò")
		
		self.assertEquals(self.pinyin_parser_mixed.getTonedVocalFromVocalAndToneNumber("u", 0), "u")
		self.assertEquals(self.pinyin_parser_mixed.getTonedVocalFromVocalAndToneNumber("u", 1), "ū")
		self.assertEquals(self.pinyin_parser_mixed.getTonedVocalFromVocalAndToneNumber("u", 2), "ú")
		self.assertEquals(self.pinyin_parser_mixed.getTonedVocalFromVocalAndToneNumber("u", 3), "ǔ")
		self.assertEquals(self.pinyin_parser_mixed.getTonedVocalFromVocalAndToneNumber("u", 4), "ù")
		
		self.assertEquals(self.pinyin_parser_mixed.getTonedVocalFromVocalAndToneNumber("U", 0), "U")
		self.assertEquals(self.pinyin_parser_mixed.getTonedVocalFromVocalAndToneNumber("U", 1), "Ū")
		self.assertEquals(self.pinyin_parser_mixed.getTonedVocalFromVocalAndToneNumber("U", 2), "Ú")
		self.assertEquals(self.pinyin_parser_mixed.getTonedVocalFromVocalAndToneNumber("U", 3), "Ǔ")
		self.assertEquals(self.pinyin_parser_mixed.getTonedVocalFromVocalAndToneNumber("U", 4), "Ù")
		
		self.assertEquals(self.pinyin_parser_mixed.getTonedVocalFromVocalAndToneNumber("ü", 0), "ü")
		self.assertEquals(self.pinyin_parser_mixed.getTonedVocalFromVocalAndToneNumber("ü", 1), "ǖ")
		self.assertEquals(self.pinyin_parser_mixed.getTonedVocalFromVocalAndToneNumber("ü", 2), "ǘ")
		self.assertEquals(self.pinyin_parser_mixed.getTonedVocalFromVocalAndToneNumber("ü", 3), "ǚ")
		self.assertEquals(self.pinyin_parser_mixed.getTonedVocalFromVocalAndToneNumber("ü", 4), "ǜ")
		
		self.assertEquals(self.pinyin_parser_mixed.getTonedVocalFromVocalAndToneNumber("Ü", 0), "Ü")
		self.assertEquals(self.pinyin_parser_mixed.getTonedVocalFromVocalAndToneNumber("Ü", 1), "Ǖ")
		self.assertEquals(self.pinyin_parser_mixed.getTonedVocalFromVocalAndToneNumber("Ü", 2), "Ǘ")
		self.assertEquals(self.pinyin_parser_mixed.getTonedVocalFromVocalAndToneNumber("Ü", 3), "Ǚ")
		self.assertEquals(self.pinyin_parser_mixed.getTonedVocalFromVocalAndToneNumber("Ü", 4), "Ǜ")
	
	def test_getLastVocalFromText (self):
		self.assertEquals(self.pinyin_parser_mixed.getLastVocalFromText("Ni3hao3ma?"), "a")
		self.assertEquals(self.pinyin_parser_mixed.getLastVocalFromText("Ni3xiang3qu4zhong1guo2ma?"), "a")
		self.assertEquals(self.pinyin_parser_mixed.getLastVocalFromText("Ni3jiao4shen2meming2zi?"), "i")
		self.assertEquals(self.pinyin_parser_mixed.getLastVocalFromText("Xian1zai4ji3dian3le?"), "e")
	
	def test_getNumberedSyllableFromTonedSyllable (self):
		self.assertEquals(self.pinyin_parser_mixed.getNumberedSyllableFromTonedSyllable("Míng"), "Ming2")
		self.assertEquals(self.pinyin_parser_mixed.getNumberedSyllableFromTonedSyllable("tiān"), "tian1")
		self.assertEquals(self.pinyin_parser_mixed.getNumberedSyllableFromTonedSyllable("nǐ"), "ni3")
		self.assertEquals(self.pinyin_parser_mixed.getNumberedSyllableFromTonedSyllable("děi"), "dei3")
		self.assertEquals(self.pinyin_parser_mixed.getNumberedSyllableFromTonedSyllable("qǐ"), "qi3")
		self.assertEquals(self.pinyin_parser_mixed.getNumberedSyllableFromTonedSyllable("chuāng"), "chuang1")
		self.assertEquals(self.pinyin_parser_mixed.getNumberedSyllableFromTonedSyllable("hěn"), "hen3")
		self.assertEquals(self.pinyin_parser_mixed.getNumberedSyllableFromTonedSyllable("zǎo"), "zao3")
		self.assertEquals(self.pinyin_parser_mixed.getNumberedSyllableFromTonedSyllable("Wǎn"), "Wan3")
		self.assertEquals(self.pinyin_parser_mixed.getNumberedSyllableFromTonedSyllable("ān"), "an1")
	
	def test_isTonedSyllable (self):
		self.assertTrue(self.pinyin_parser_mixed.isTonedSyllable("lōng"))
		self.assertTrue(self.pinyin_parser_mixed.isTonedSyllable("lóng"))
		self.assertTrue(self.pinyin_parser_mixed.isTonedSyllable("lǒng"))
		self.assertTrue(self.pinyin_parser_mixed.isTonedSyllable("lòng"))
		
		self.assertTrue(self.pinyin_parser_mixed.isTonedSyllable("Lōng"))
		self.assertTrue(self.pinyin_parser_mixed.isTonedSyllable("Lóng"))
		self.assertTrue(self.pinyin_parser_mixed.isTonedSyllable("Lǒng"))
		self.assertTrue(self.pinyin_parser_mixed.isTonedSyllable("Lòng"))
		
		self.assertTrue(self.pinyin_parser_mixed.isTonedSyllable("ān"))
		self.assertTrue(self.pinyin_parser_mixed.isTonedSyllable("án"))
		self.assertTrue(self.pinyin_parser_mixed.isTonedSyllable("ǎn"))
		self.assertTrue(self.pinyin_parser_mixed.isTonedSyllable("àn"))
		
		self.assertTrue(self.pinyin_parser_mixed.isTonedSyllable("Ān"))
		self.assertTrue(self.pinyin_parser_mixed.isTonedSyllable("Án"))
		self.assertTrue(self.pinyin_parser_mixed.isTonedSyllable("Ǎn"))
		self.assertTrue(self.pinyin_parser_mixed.isTonedSyllable("Àn"))
		
		self.assertFalse(self.pinyin_parser_mixed.isTonedSyllable("long"))
		self.assertFalse(self.pinyin_parser_mixed.isTonedSyllable("Long"))
		self.assertFalse(self.pinyin_parser_mixed.isTonedSyllable("an"))
		self.assertFalse(self.pinyin_parser_mixed.isTonedSyllable("An"))
		
	def test_isNumberedSyllable (self):
		self.assertTrue(self.pinyin_parser_mixed.isNumberedSyllable("xiao0"))
		self.assertTrue(self.pinyin_parser_mixed.isNumberedSyllable("xiao1"))
		self.assertTrue(self.pinyin_parser_mixed.isNumberedSyllable("xiao2"))
		self.assertTrue(self.pinyin_parser_mixed.isNumberedSyllable("xiao3"))
		self.assertTrue(self.pinyin_parser_mixed.isNumberedSyllable("xiao4"))
		
		self.assertTrue(self.pinyin_parser_mixed.isNumberedSyllable("Xiao0"))
		self.assertTrue(self.pinyin_parser_mixed.isNumberedSyllable("Xiao1"))
		self.assertTrue(self.pinyin_parser_mixed.isNumberedSyllable("Xiao2"))
		self.assertTrue(self.pinyin_parser_mixed.isNumberedSyllable("Xiao3"))
		self.assertTrue(self.pinyin_parser_mixed.isNumberedSyllable("Xiao4"))
		
		self.assertTrue(self.pinyin_parser_mixed.isNumberedSyllable("yi0"))
		self.assertTrue(self.pinyin_parser_mixed.isNumberedSyllable("yi1"))
		self.assertTrue(self.pinyin_parser_mixed.isNumberedSyllable("yi2"))
		self.assertTrue(self.pinyin_parser_mixed.isNumberedSyllable("yi3"))
		self.assertTrue(self.pinyin_parser_mixed.isNumberedSyllable("yi4"))
		
		self.assertTrue(self.pinyin_parser_mixed.isNumberedSyllable("Yi0"))
		self.assertTrue(self.pinyin_parser_mixed.isNumberedSyllable("Yi1"))
		self.assertTrue(self.pinyin_parser_mixed.isNumberedSyllable("Yi2"))
		self.assertTrue(self.pinyin_parser_mixed.isNumberedSyllable("Yi3"))
		self.assertTrue(self.pinyin_parser_mixed.isNumberedSyllable("Yi4"))
		
		
		self.assertFalse(self.pinyin_parser_mixed.isNumberedSyllable("xiāo"))
		self.assertFalse(self.pinyin_parser_mixed.isNumberedSyllable("xiáo"))
		self.assertFalse(self.pinyin_parser_mixed.isNumberedSyllable("xiǎo"))
		self.assertFalse(self.pinyin_parser_mixed.isNumberedSyllable("xiào"))
		
		self.assertFalse(self.pinyin_parser_mixed.isNumberedSyllable("Xiāo"))
		self.assertFalse(self.pinyin_parser_mixed.isNumberedSyllable("Xiáo"))
		self.assertFalse(self.pinyin_parser_mixed.isNumberedSyllable("Xiǎo"))
		self.assertFalse(self.pinyin_parser_mixed.isNumberedSyllable("Xiào"))
		
		self.assertFalse(self.pinyin_parser_mixed.isNumberedSyllable("yī"))
		self.assertFalse(self.pinyin_parser_mixed.isNumberedSyllable("yí"))
		self.assertFalse(self.pinyin_parser_mixed.isNumberedSyllable("yǐ"))
		self.assertFalse(self.pinyin_parser_mixed.isNumberedSyllable("yì"))
		
		self.assertFalse(self.pinyin_parser_mixed.isNumberedSyllable("Yī"))
		self.assertFalse(self.pinyin_parser_mixed.isNumberedSyllable("Yí"))
		self.assertFalse(self.pinyin_parser_mixed.isNumberedSyllable("Yǐ"))
		self.assertFalse(self.pinyin_parser_mixed.isNumberedSyllable("Yì"))
		
	def test_getToneNumberFromTonedSyllable (self):
		self.assertEquals(self.pinyin_parser_mixed.getToneNumberFromTonedSyllable("Tā"), "1")
		self.assertEquals(self.pinyin_parser_mixed.getToneNumberFromTonedSyllable("Tá"), "2")
		self.assertEquals(self.pinyin_parser_mixed.getToneNumberFromTonedSyllable("Tǎ"), "3")
		self.assertEquals(self.pinyin_parser_mixed.getToneNumberFromTonedSyllable("Tà"), "4")
		
		self.assertEquals(self.pinyin_parser_mixed.getToneNumberFromTonedSyllable("tā"), "1")
		self.assertEquals(self.pinyin_parser_mixed.getToneNumberFromTonedSyllable("tá"), "2")
		self.assertEquals(self.pinyin_parser_mixed.getToneNumberFromTonedSyllable("tǎ"), "3")
		self.assertEquals(self.pinyin_parser_mixed.getToneNumberFromTonedSyllable("tà"), "4")
		
		self.assertEquals(self.pinyin_parser_mixed.getToneNumberFromTonedSyllable("Zhōng"), "1")
		self.assertEquals(self.pinyin_parser_mixed.getToneNumberFromTonedSyllable("Zhóng"), "2")
		self.assertEquals(self.pinyin_parser_mixed.getToneNumberFromTonedSyllable("Zhǒng"), "3")
		self.assertEquals(self.pinyin_parser_mixed.getToneNumberFromTonedSyllable("Zhòng"), "4")
		
		self.assertEquals(self.pinyin_parser_mixed.getToneNumberFromTonedSyllable("zhōng"), "1")
		self.assertEquals(self.pinyin_parser_mixed.getToneNumberFromTonedSyllable("zhóng"), "2")
		self.assertEquals(self.pinyin_parser_mixed.getToneNumberFromTonedSyllable("zhǒng"), "3")
		self.assertEquals(self.pinyin_parser_mixed.getToneNumberFromTonedSyllable("zhòng"), "4")
		
	def test_getPlainSyllableFromTonedSyllable (self):
		self.assertEquals(self.pinyin_parser_mixed.getPlainSyllableFromTonedSyllable("Míng"), "Ming")
		self.assertEquals(self.pinyin_parser_mixed.getPlainSyllableFromTonedSyllable("tiān"), "tian")
		self.assertEquals(self.pinyin_parser_mixed.getPlainSyllableFromTonedSyllable("nǐ"), "ni")
		self.assertEquals(self.pinyin_parser_mixed.getPlainSyllableFromTonedSyllable("děi"), "dei")
		self.assertEquals(self.pinyin_parser_mixed.getPlainSyllableFromTonedSyllable("qǐ"), "qi")
		self.assertEquals(self.pinyin_parser_mixed.getPlainSyllableFromTonedSyllable("chuāng"), "chuang")
		self.assertEquals(self.pinyin_parser_mixed.getPlainSyllableFromTonedSyllable("hěn"), "hen")
		self.assertEquals(self.pinyin_parser_mixed.getPlainSyllableFromTonedSyllable("zǎo"), "zao")
		self.assertEquals(self.pinyin_parser_mixed.getPlainSyllableFromTonedSyllable("Wǎn"), "Wan")
		self.assertEquals(self.pinyin_parser_mixed.getPlainSyllableFromTonedSyllable("ān"), "an")
		self.assertEquals(self.pinyin_parser_mixed.getPlainSyllableFromTonedSyllable("an"), "an")
		self.assertEquals(self.pinyin_parser_mixed.getPlainSyllableFromTonedSyllable("ā2n"), "a2n")
		self.assertEquals(self.pinyin_parser_mixed.getPlainSyllableFromTonedSyllable("a2n"), "a2n")
	
	def test_getPlainSyllableFromNumberedSyllable (self):
		self.assertEquals(self.pinyin_parser_mixed.getPlainSyllableFromNumberedSyllable("Ming2"), "Ming")
		self.assertEquals(self.pinyin_parser_mixed.getPlainSyllableFromNumberedSyllable("tian1"), "tian")
		self.assertEquals(self.pinyin_parser_mixed.getPlainSyllableFromNumberedSyllable("ni3"), "ni")
		self.assertEquals(self.pinyin_parser_mixed.getPlainSyllableFromNumberedSyllable("dei3"), "dei")
		self.assertEquals(self.pinyin_parser_mixed.getPlainSyllableFromNumberedSyllable("qi3"), "qi")
		self.assertEquals(self.pinyin_parser_mixed.getPlainSyllableFromNumberedSyllable("chuang1"), "chuang")
		self.assertEquals(self.pinyin_parser_mixed.getPlainSyllableFromNumberedSyllable("hen3"), "hen")
		self.assertEquals(self.pinyin_parser_mixed.getPlainSyllableFromNumberedSyllable("zao3"), "zao")
		self.assertEquals(self.pinyin_parser_mixed.getPlainSyllableFromNumberedSyllable("Wan3"), "Wan")
		self.assertEquals(self.pinyin_parser_mixed.getPlainSyllableFromNumberedSyllable("an1"), "an")
		self.assertEquals(self.pinyin_parser_mixed.getPlainSyllableFromNumberedSyllable("hao4"), "hao")
		self.assertEquals(self.pinyin_parser_mixed.getPlainSyllableFromNumberedSyllable("hao0"), "hao")
		self.assertEquals(self.pinyin_parser_mixed.getPlainSyllableFromNumberedSyllable("ha21o0"), "ha21o")
	
	def test_getTonedVocalOfTonedSyllable (self):
		self.assertEquals(self.pinyin_parser_mixed.getTonedVocalOfTonedSyllable("Míng"), "í")
		self.assertEquals(self.pinyin_parser_mixed.getTonedVocalOfTonedSyllable("tiān"), "ā")
		self.assertEquals(self.pinyin_parser_mixed.getTonedVocalOfTonedSyllable("nǐ"), "ǐ")
		self.assertEquals(self.pinyin_parser_mixed.getTonedVocalOfTonedSyllable("děi"), "ě")
		self.assertEquals(self.pinyin_parser_mixed.getTonedVocalOfTonedSyllable("qǐ"), "ǐ")
		self.assertEquals(self.pinyin_parser_mixed.getTonedVocalOfTonedSyllable("chuāng"), "ā")
		self.assertEquals(self.pinyin_parser_mixed.getTonedVocalOfTonedSyllable("hěn"), "ě")
		self.assertEquals(self.pinyin_parser_mixed.getTonedVocalOfTonedSyllable("zǎo"), "ǎ")
		self.assertEquals(self.pinyin_parser_mixed.getTonedVocalOfTonedSyllable("Wǎn"), "ǎ")
		self.assertEquals(self.pinyin_parser_mixed.getTonedVocalOfTonedSyllable("ān"), "ā")
		
	def test_isNonSyllableCharacter (self):
		
		ignorable_characters = [
			'.', ',', '?', '!', ':', '-', ';', '…', '·', '–', '~',
			'。', '，', '、', '？', '！',
			'\"', '\'', '“', '”', '‘', '’', '´', '`',
			'/','\\',
			'(',')','[',']','{','}',
			' ',
			'\n','\t'
		]
		
		tone_numbers = ["0","1","2","3","4"]
		
		other_digits = ["5", "6", "7", "8", "9"]
		
		for ignorable_character in ignorable_characters:
			self.assertTrue(self.pinyin_parser_mixed.isValidNonSyllableCharacter(ignorable_character))
		
		for tone_number in tone_numbers:
			self.assertTrue(self.pinyin_parser_mixed.isValidNonSyllableCharacter(tone_number))
			
		for other_digit in other_digits:
			self.assertTrue(self.pinyin_parser_mixed.isValidNonSyllableCharacter(other_digit))
		
		self.assertFalse(self.pinyin_parser_mixed.isValidNonSyllableCharacter('a'))
		self.assertFalse(self.pinyin_parser_mixed.isValidNonSyllableCharacter('b'))
		self.assertFalse(self.pinyin_parser_mixed.isValidNonSyllableCharacter('c'))
		self.assertFalse(self.pinyin_parser_mixed.isValidNonSyllableCharacter('d'))
		self.assertFalse(self.pinyin_parser_mixed.isValidNonSyllableCharacter('e'))
		self.assertFalse(self.pinyin_parser_mixed.isValidNonSyllableCharacter('f'))
		
	def test_getTonedSyllableFromNumberedSyllable (self):
		self.assertEquals(self.pinyin_parser_mixed.getTonedSyllableFromNumberedSyllable("Ni3"), "Nǐ")
		self.assertEquals(self.pinyin_parser_mixed.getTonedSyllableFromNumberedSyllable("hao3"), "hǎo")
		self.assertEquals(self.pinyin_parser_mixed.getTonedSyllableFromNumberedSyllable("ma"), "ma")
		self.assertEquals(self.pinyin_parser_mixed.getTonedSyllableFromNumberedSyllable("Zhe4"), "Zhè")
		self.assertEquals(self.pinyin_parser_mixed.getTonedSyllableFromNumberedSyllable("shi4"), "shì")
		self.assertEquals(self.pinyin_parser_mixed.getTonedSyllableFromNumberedSyllable("yi1"), "yī")
		self.assertEquals(self.pinyin_parser_mixed.getTonedSyllableFromNumberedSyllable("wei4"), "wèi")
		self.assertEquals(self.pinyin_parser_mixed.getTonedSyllableFromNumberedSyllable("jiao4"), "jiào")
		self.assertEquals(self.pinyin_parser_mixed.getTonedSyllableFromNumberedSyllable("shou4"), "shòu")
		
	def test_getToneNumberOfSyllable (self):
		self.assertEquals(self.pinyin_parser_mixed.getToneNumberOfSyllable("ma"), 0)
		self.assertEquals(self.pinyin_parser_mixed.getToneNumberOfSyllable("ma1"), 1)
		self.assertEquals(self.pinyin_parser_mixed.getToneNumberOfSyllable("ming2"), 2)
		self.assertEquals(self.pinyin_parser_mixed.getToneNumberOfSyllable("ni3"), 3)
		self.assertEquals(self.pinyin_parser_mixed.getToneNumberOfSyllable("jiao4"), 4)
		
		self.assertEquals(self.pinyin_parser_mixed.getToneNumberOfSyllable("Ma"), 0)
		self.assertEquals(self.pinyin_parser_mixed.getToneNumberOfSyllable("Ma1"), 1)
		self.assertEquals(self.pinyin_parser_mixed.getToneNumberOfSyllable("Ming2"), 2)
		self.assertEquals(self.pinyin_parser_mixed.getToneNumberOfSyllable("Ni3"), 3)
		self.assertEquals(self.pinyin_parser_mixed.getToneNumberOfSyllable("Jiao4"), 4)