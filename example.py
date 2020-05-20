"""Example file to learn how to work with the Library.

Is using example dataset from datasets folder, but you
can import yours.
"""

from Tree import Node, insert, search
from Fer import Corrector, tokenize_file

data = tokenize_file('datasets/ggm.txt')

cr = Corrector(data)

cr.build_tree()

print(cr.correct('zarcazo'))