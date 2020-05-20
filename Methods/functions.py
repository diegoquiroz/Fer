"""
@created_by: Diego Quiroz
			 diego00aq@gmail.com
@created: 05-20-2020
@modified: 05-21-2020
"""

""" Regex Library to process text """
import re


"""This function reads the information from the file
and calls tokenize_text function to tokenize it.

:param path_to_file: str of the file path
:return data: a list of all the tokenized data
"""
def tokenize_file( path_to_file):
	data = tokenize_text(
		open(path_to_file).read())
	return data

"""This function reads raw text, convert it to lower case
and eliminates all the non-alphanumeric characters.

:param string: str to tokenize.
:return: a list of all the tokenized data
"""
def tokenize_text( text):
	return re.findall(r'\w+', text.lower())
