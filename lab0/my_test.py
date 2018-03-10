from lab0 import count_pattern

# Assignment info:
# https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-034-artificial-intelligence-fall-2010/assignments/MIT6_034F10_lab0.pdf

assert count_pattern( ('a', 'b'), ('a', 'b', 'c', 'e', 'b', 'a', 'b', 'f')) == 2
assert count_pattern( ('a', 'b'), ('a', 'b', 'ab', 'e', 'b', 'a', 'b', 'f')) == 2
assert count_pattern( ('a', 'b'), ('a', 'b')) == 1
assert count_pattern( ('a'), ('a')) == 1
assert count_pattern( ('a'), ()) == 0

assert count_pattern(('a', 'b', 'a'), ('g', 'a', 'b', 'a', 'b', 'a', 'b', 'a')) == 3
assert count_pattern(('a', 'b', 'a', 'b'), ('a', 'b', 'a', 'b', 'a', 'b', 'a')) == 2
