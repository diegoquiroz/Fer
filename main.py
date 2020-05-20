from Tree import Node, insert, search
from Fer import Corrector, tokenize_file

data = tokenize_file('ggm.txt')

cr = Corrector(data)

cr.build_tree()

print(cr.correct('zarcazo'))