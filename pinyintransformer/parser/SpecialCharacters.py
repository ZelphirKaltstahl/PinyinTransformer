__author__ = 'xiaolong'

from enum import Enum

class SpecialCharacters(Enum):
	
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