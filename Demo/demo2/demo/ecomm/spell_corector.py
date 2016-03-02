import pandas as pd
import enchant
import re, collections
from nltk.metrics import edit_distance
from fuzzywuzzy import process


class checkspell(object):
	def __init__(self,dict_name,max_dist):
		df = pd.read_csv("dict2.txt",header=None,sep="@",skip_blank_lines=True)
		df.columns = ['key','value']
		dic = df.set_index('key')['value'].to_dict()
		file_read = open('words.txt').read().split('\n')
		filelist = [x.strip() for x in file_read]
		self.spelling_dict = enchant.Dict(dict_name)
		self.max_dist = max_dist
		self.dic = dic
		self.filelist = filelist
		self.NWORDS = self.train(self.words(file('train.txt').read()))
		# print type(self.NWORDS['lance'])
		self.alphabet = 'abcdefghijklmnopqrstuvwxyz'
		
	def meaning(self,word):
		result_list = list()
		# print word + "in here"
		if word in self.dic:
			return self.dic[word]
		else:
			for i in range(1,4):
				result_word = word + str(i)
				if result_word in self.dic:
					result_list.append(self.dic[result_word])
		# print result_word
		return result_list

	def checks(self,word):
		suggest_list =list()
		# print type(self.spelling_dict.check(word))
		if self.spelling_dict.check(word):
			return self.meaning(word)
		suggestions = self.spelling_dict.suggest(word)
		# print suggestions
		for suggest in suggestions:
			if suggest and edit_distance(word,suggest) <= self.max_dist:
				# print "in"
				suggest_list.append(suggest)
		if suggest_list:
			# print suggest_list
			return suggest_list
		else:
			return word

	def nearest_word(self,word):
		if self.spelling_dict.check(word):
			return self.meaning(word)

		x = process.extract(word,self.filelist, limit=20)
		l=len(word)
		# print x
		result = [a for a,b in x if not len(a)<l][:5]
		return result,x[:5]

	def add_word(self,word):
		self.filelist.append(word)
		self.NWORDS['word'] += 1
		return True

	def words(self,text): return re.findall('[a-z]+', text.lower())

	def train(self,features):
		model = collections.defaultdict(lambda: 1)
		for f in features:
		    model[f] += 1
		return model

	def edits1(self,word):
		splits     = [(word[:i], word[i:]) for i in range(len(word) + 1)]
		deletes    = [a + b[1:] for a, b in splits if b]
		transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b)>1]
		replaces   = [a + c + b[1:] for a, b in splits for c in self.alphabet if b]
		inserts    = [a + c + b     for a, b in splits for c in self.alphabet]
		return set(deletes + transposes + replaces + inserts)

	def known_edits2(self,word):
		return set(e2 for e1 in self.edits1(word) for e2 in self.edits1(e1) if e2 in self.NWORDS)

	def known(self,words): return set(w for w in words if w in self.NWORDS)

	def correct(self,word):
		candidates = self.known([word]) or self.known(self.edits1(word)) or self.known_edits2(word) or [word]
		return max(candidates, key=self.NWORDS.get)
