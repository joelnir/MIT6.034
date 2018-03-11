from lab0 import count_pattern, depth, tree_ref

# Assignment info:
# https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-034-artificial-intelligence-fall-2010/assignments/MIT6_034F10_lab0.pdf

assert count_pattern( ('a', 'b'), ('a', 'b', 'c', 'e', 'b', 'a', 'b', 'f')) == 2
assert count_pattern( ('a', 'b'), ('a', 'b', 'ab', 'e', 'b', 'a', 'b', 'f')) == 2
assert count_pattern( ('a', 'b'), ('a', 'b')) == 1
assert count_pattern( ('a'), ('a')) == 1
assert count_pattern( ('a'), ()) == 0
assert count_pattern(('a', 'b', 'a'), ('g', 'a', 'b', 'a', 'b', 'a', 'b', 'a')) == 3
assert count_pattern(('a', 'b', 'a', 'b'), ('a', 'b', 'a', 'b', 'a', 'b', 'a')) == 2


assert depth('x') == 0
assert depth(('expt', 'x', 2)) == 1
assert depth(('+', ('expt', 'x', 2), ('expt', 'y', 2))) == 2
assert depth(('/', ('expt', 'x', 5), ('expt', ('-', ('expt', 'x', 2), 1), ('/', 5, 2)))) == 4

assert depth(('a', ('a', ('b', ('c', 2))), ('a', 'b'))) == 4
assert depth(()) == 0

tree = (((1, 2), 3), (4, (5, 6)), 7, (8, 9, 10))
assert tree_ref(tree, (3, 1)) == 9
assert tree_ref(tree, (1, 1, 1)) == 6
assert tree_ref(tree, (0,)) == ((1, 2), 3)
