"""
@created_by: Diego Quiroz
			 diego00aq@gmail.com
@created: 05-20-2020
@modified: 05-21-2020
"""

""" Tree data structure """
from Tree import Node, insert, search

class Corrector(object):

	"""Constructor of Class Corrector.
	
	:var data: list of all the data in the Corpus
	:var letters: saves all the letters in the alphabet
	"""
	def __init__(self, data):
		self.data = data
		self.tree_root = None
		self.letters = 'abcdefghijklmnñopqrstuvwxyz'

	"""This function is in charge to build the tree from
	the list of data. Modifies the value of Corrector.tree_root
	variable.

	:Public
	"""
	def build_tree(self):
		self.tree_root = Node(self.data[0])
		for i in range(len(self.data)):
			insert(self.tree_root, Node(self.data[i]))
	
	"""This function returns the candidates of corrections,
	prioritizing the ones with 1 Levenshtein distance.

	:Private:
	:param word: the word to be corrected.
	"""
	def _candidates(self, word): 
	    if self.__known([word]):
	      return self.__known([word])
	    elif self.__known(self.__d1_posibilities(word)):
	      return self.__known(self.__d1_posibilities(word))
	    elif self.__known(self.__d2_posibilities(word)):
	      return self.__known(self.__d2_posibilities(word))
	    elif [word]:
	      return [word]

	"""This function returns the words that match with
	the ones we know in the Tree.

	:Private!:
	:param words: hash map (set()) of the words we want
	to know if matches.
	:return: list of the words that match.
	"""
	def __known(self, words):
	    return [w for w in words if search(self.tree_root,w)]

	"""This function returns all the permutations with
	Levenshtein distance of 1.

	:Private!:
	:param word: the word to correct.
	:return: hash map (set()) of the permutations.
	"""
	def __d1_posibilities(self, word):
	    word_length = len(word)
	    splits = [(word[:i], word[i:]) for i in range(word_length+1)]
	    deletes = [L + R[1:] for L, R in splits if R]
	    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
	    replaces = [L + c + R[1:] for L, R in splits if R for c in self.letters]
	    inserts = [L + c + R for L, R in splits for c in self.letters]
	    return set(deletes + transposes + replaces + inserts)

	"""This function returns all the permutations with
	Levenshtein distance of 2.

	:Private!:
	:param word: the word to correct.
	:return: hash map (set()) of the permutations.
	"""
	def __d2_posibilities(self, word): 
	    return set(e2 for e1 in self.__d1_posibilities(word) for e2 in self.__d1_posibilities(e1))

	"""This function returns the first candidate.
	TODO: calculate this by relevance instead of
	returning always the first one.

	:param word: string with the word to correct
	:return first_candidate: the first word in
	the list of candidate words
	"""
	def correct(self, word):
		first_candidate = self._candidates(word)[0]
		return first_candidate
	
	"""This function returns the parameter data of
	this class.

	:return data: list of complete list of data.
	"""
	def get_data(self):
		return self.data

	"""This function changes the value of parameter
	data.

	:param new_data: list of the new data to be used
	in the class.
	"""
	def set_data(self, new_data):
		self.data = new_data

	"""This function returns the root of the tree once built.

	:return tree_root: Node object
	"""
	def get_tree_root(self):
		return self.tree_root

	"""This function changes the value of parameter
	new_root.

	:param new_root: Node of the new root to be used
	in the class.
	"""
	def set_tree_root(self, new_root):
		self.tree_root = new_root
